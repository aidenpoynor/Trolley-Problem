const { Storage } = require("@google-cloud/storage");
const csv = require("fast-csv");
const fs = require("fs");
const os = require("os");

// Initialize GCS client
const storage = new Storage();
const bucketName = "your-bucket-name";
const fileName = "survey_responses.csv";

exports.saveSurveyResponse = async (req, res) => {
    if (req.method !== "POST") {
        return res.status(405).send("Method Not Allowed");
    }

    const { questionNumbers, answer } = req.body;

    if (!questionNumbers || !answer) {
        return res.status(400).send("Invalid request: Missing data.");
    }

    try {
        // Temporary local file
        const tempFilePath = `${os.tmpdir()}/${fileName}`;
        const bucket = storage.bucket(bucketName);
        const file = bucket.file(fileName);

        // Check if the CSV exists
        const [exists] = await file.exists();

        if (exists) {
            // Download the existing file
            await file.download({ destination: tempFilePath });
        }

        // Append new data
        const writeStream = fs.createWriteStream(tempFilePath, { flags: "a" });
        csv.writeToStream(writeStream, [[...questionNumbers, answer]], { headers: !exists });

        await new Promise((resolve, reject) => {
            writeStream.on("finish", resolve);
            writeStream.on("error", reject);
        });

        // Upload the updated file back to GCS
        await bucket.upload(tempFilePath, { destination: fileName });

        // Clean up the temporary file
        fs.unlinkSync(tempFilePath);

        res.status(200).send("Response saved successfully.");
    } catch (error) {
        console.error("Error saving response:", error);
        res.status(500).send("Internal Server Error");
    }
};

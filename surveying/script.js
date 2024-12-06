// Get references to DOM elements
const generateBtn = document.getElementById("generate-btn");
const numberDisplay = document.getElementById("number-display");
const answerSection = document.getElementById("answer-section");
const yesBtn = document.getElementById("yes-btn");
const noBtn = document.getElementById("no-btn");
const responseList = document.getElementById("response-list");

// Store the generated number and responses
let prompt = null;
const responses = [];

function generateQuestion() {
  var num_on_main = Math.floor(Math.random() * 5) + 1;
  var num_on_alt = Math.floor(Math.random() * 5) + 1;

  var relationship_main = Math.floor(Math.random() * 4) + 1;
  var relationship_alt = Math.floor(Math.random() * 4) + 1;

  var harm_severity_main = Math.round(Math.random());
  var harm_severity_alt = Math.round(Math.random());

  var social_pressure = Math.round(Math.random());

  var social_importance_main = Math.floor(Math.random() * 5) + 1;
  var social_importance_alt = Math.floor(Math.random() * 5) + 1;

  prompt = gen_prompt(num_on_main,num_on_alt,relationship_main,relationship_alt,harm_severity_main,harm_severity_alt,social_pressure,social_importance_main,social_importance_alt);

  numberDisplay.innerHTML = prompt.formattedPrompt; // Use innerHTML to parse and render the HTML tags
  answerSection.style.display = "block";
}

function get_relationship(relationship) {
  switch (relationship) {
    case 1:
      return "Total Stranger";
    case 2:
      return "Acquaintance";
    case 3:
      return "Friend";
    case 4:
      return "Loved One";
  }
}

function get_social_status(status) {
  switch (status) {
    case 1:
      return "Murderer";
    case 2:
      return "Thief";
    case 3:
      return "Average Joe";
    case 4:
      return "Upstanding Citizen";
    case 5:
      return "Doctor";
  }
}

function get_harm(harm) {
  switch (harm) {
    case 0:
      return "Slow and Painful Death";
    case 1:
      return "Instant Death";
  }
}

function get_pressure(pressure) {
  switch (pressure) {
    case 0:
      return "Nobody is around to see your decision";
    case 1:
      return "Tons of people are watching your decision";
  }
}

function gen_prompt(num_on_main, num_on_alt, relationship_main, relationship_alt, harm_severity_main, harm_severity_alt, social_pressure, social_importance_main, social_importance_alt) {
  const formattedPrompt = "Status of Main Rail:<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Number of people: " + num_on_main + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Relationship to Them: " + get_relationship(relationship_main) + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Group Social Status: " + get_social_status(social_importance_main) + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Harm on Collision: " + get_harm(harm_severity_main) + "<br><br>" +

  "Status of Alternate Rail:<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Number of people: " + num_on_alt + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Relationship to Them: " + get_relationship(relationship_alt) + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Group Social Status: " + get_social_status(social_importance_alt) + "<br>" + 
  "&nbsp;&nbsp;&nbsp;&nbsp;Harm on Collision: " + get_harm(harm_severity_alt) + "<br><br>" + get_pressure(social_pressure);
  
  return {
  formattedPrompt: formattedPrompt,
  numbers: {
    num_on_main,
    num_on_alt,
    relationship_main,
    relationship_alt,
    harm_severity_main,
    harm_severity_alt,
    social_pressure,
    social_importance_main,
    social_importance_alt
    }
  };
}


// Function to convert numbers and answer to a CSV format
function convertToCSVRow(numbers, answer) {
  if (answer == "Yes") {
    answer = 1;
  } else {
    answer = 0;
  }
  return [
    numbers.num_on_main,
    numbers.num_on_alt,
    numbers.relationship_main,
    numbers.relationship_alt,
    numbers.harm_severity_main,
    numbers.harm_severity_alt,
    numbers.social_pressure,
    numbers.social_importance_main,
    numbers.social_importance_alt,
    answer
  ].join(",");
}
function convertToArray(numbers) {

  return [
    numbers.num_on_main,
    numbers.num_on_alt,
    numbers.relationship_main,
    numbers.relationship_alt,
    numbers.harm_severity_main,
    numbers.harm_severity_alt,
    numbers.social_pressure,
    numbers.social_importance_main,
    numbers.social_importance_alt
  ];
}

const cloudFunctionUrl = 'insert-URL';

function handleResponse(answer) {
  if (prompt !== null) {
    // Construct the payload
    const data = {
      questionNumbers: convertToArray(prompt.numbers), // Array of numbers from your generated prompt
      answer: answer, // User's answer ('Yes' or 'No')
    };

    // Send the data to the Cloud Function
    fetch(cloudFunctionUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.text();
      })
      .then((responseText) => {
        console.log('Response from Cloud Function:', responseText);
      })
      .catch((error) => {
        console.error('Error sending data to Cloud Function:', error);
      });

    // Update the UI
    responses.push({ question: prompt.numbers, answer });

    const listItem = document.createElement('li');
    listItem.innerHTML = convertToCSVRow(prompt.numbers, answer);
    responseList.appendChild(listItem);

    numberDisplay.textContent = '';
    answerSection.style.display = 'none';
    prompt = null;
  }
}


// Attach event listeners
generateBtn.addEventListener("click", generateQuestion);
yesBtn.addEventListener("click", () => handleResponse("Yes"));
noBtn.addEventListener("click", () => handleResponse("No"));

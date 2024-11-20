import KNN
import sys
import csv
from survey import Survey

def usage():
    print("Here are your options:")
    print("train    -   train KNN model")
    print("predict  -   see what the KNN model would do in a random situation")
    print("survey   -   decide what you would do in a random trolly problem and give it to the model")
    print("exit     -   exit program")


if __name__ == "__main__":

    model = None
    
    
    #data = "trolley.csv"
    data = "dummy_data.csv"
    survey = "survey.csv"

    if data != "trolley.csv":
        print(f"Warning! You are working with {data} for you dataset!")

    while True:
        print("What would you like to do?")
        usage()
        action = input()

        match action.lower():

            case "exit":
                print("Goodbye!")
                sys.exit()
            case "train":
                print("Creating KNN model...")
                model = KNN.KNN(data)
            case "predict":
                if model == None:
                    print("No current model!")
                else: model.predict()
            case "survey":

                print("\nWhat would you do in the following scenarios...\n\n\n")
                survey = Survey(3)
                print(survey.info)

                # Open the CSV file in write mode
                with open(data, "a", newline="") as file:

                    # Create a CSV writer object
                    writer = csv.writer(file)


                    # Write the data rows
                    writer.writerows(survey.info)

            case _:
                usage()


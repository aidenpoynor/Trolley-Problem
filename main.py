import KNN
import sys

if __name__ == "__main__":

    model = None
    data = "trolley.csv"
    while True:
        print("What would you like to do?")
        action = input()

        match action.lower():

            case "exit":
                print("Goodbye!")
                sys.exit()
            case "train":
                model = KNN.KNN(data)


            case "predict":
                if model == None:
                    print("No current model!")
                else: model.predict()

            case _:
                print("Here are your options:")
                print("train    -   train KNN model")
                print("predict  -   see what the KNN model would do in a random situation")
                print("survey   -   decide what you would do in a random trolly problem and give it to the model")
                print("exit     -   exit program")
import KNN,sys, csv, time, os
import analysis
from DecisionTree import DecisionTree
from survey import Survey
from pyfiglet import Figlet

##formats user input
def usage():
    print("Here are your options:")
    print("train     -   train a model")
    print("predict   -   see what the KNN model would do in a random situation")
    print("analysis  -   run trained model through a bunch of simulations and get report for results")
    print("visualize -   see visualiziton of how model makes it's decisions")
    print("load      -   customize or load in specific scenario")
    print("survey    -   decide what you would do in a random trolley problem and give it to the model")
    print("exit      -   exit program\n\n")



if __name__ == "__main__":

    model = None
    
    ## Loads dataset    
    #data = "trolley.csv"
    data = "dummy_data.csv"
    survey = "survey.csv"

    if data != "trolley.csv":
        print(f"Warning! You are working with {data} for you dataset!")

    ##programe loop
    while True:

        # Clearing the Screen
        os.system('clear')
        
        f = Figlet(font='slant')
        print(f.renderText('Trolley Problem AI'))

        ##gathers input
        print("What would you like to do?\n")
        usage()
        action = input()
        wait = False

        ##Action handeler
        match action.lower():

            case "exit":
                print("Goodbye!")
                sys.exit()

            ##Trains new model 
            case "train":

                choice = input("which model would you like to train? (K)NN or (D)ecision Tree? ")
                
                if choice.lower() == "k":
                    print("Creating KNN model...")
                    model = KNN.KNN(data)

                elif choice.lower() == 'd':
                    print("Creating Decision Tree model...")
                    model= DecisionTree(data)

                else: print("Invalid input!")
                print("Model created!")
                wait = True
            
            ##generate random trolley problem for model
            case "predict":
                
                
                if model == None:
                    print("No current model!")
                    wait = True
                else:
                    os.system('clear')
                    Survey(1,'c',model)
                    

            ##generates questions to feed back into model
            case "survey":
                os.system('clear')

                print("\nWhat would you do in the following scenarios...\n\n\n")
                survey = Survey(3)
                print(survey.info)

                # Open the CSV file in write mode
                with open(data, "a", newline="") as file:

                    # Create a CSV writer object
                    writer = csv.writer(file)

                    # Write the data rows
                    writer.writerows(survey.info)

            ##shows graphs visualization
            case "visualize":

                if model != None: model.visualize()
                else: print("No current model!")

            ##load or customize trolley problem
            case "load":

                if model != None:
                    choice = input("Would you like (l)oad a scenario or (c)ustomize one?")

                    if choice.lower() == 'l' or choice.lower()=='c':
                            Survey(0,'c',model,False,choice)
                            
                    else: print("Invalid input!")
                
                else: print("No current model!") 

            ##generate 100 random trolley problems and look at statistics
            case "analysis":
                os.system('clear')
                data = []
                wait = True
                if model == None:
                    print("No current model!")
                    break

                analysis.run_analysis(model)

            case _:
                usage()

        ##pauses for user to read any feedback before resetting
        
        if wait: time.sleep(2)
        


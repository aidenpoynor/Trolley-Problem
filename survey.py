import random
import time
import os
import pandas as pd

class Survey:

    def __init__(self, quant_questions=1,interviewee='h', model = None, hide = False, custom=None):

        self.model = model # if human is answering, should always be None
        self.hide = hide
        self.invterviewee = interviewee # 'h' for human and 'c' for cpu
        self.info = []


        self.classes = ["num_on_main",
                        "num_on_alt",
                        "relationship_main",
                        "relationship_alt",
                        "harm_severity_main",
                        "harm_severity_alt",
                        "social_pressure",
                        "social_importance_main",
                        "social_importance_alt",
                        "decision"]
        
        if custom != None:
            if custom == 'l':
                self.load()
            else: self.build_quesiton()
        else:
            for question in range(0,quant_questions):
                self.info.append(self.gen_question())

    ##implement these later
    def load(self):

        ##grabs all csv files of different scenarios
        sit_list = os.listdir("situations")

        while True:
            option = 0
            os.system('clear')
            print("List of current available trolley problems you can load:\n")
            for sit in sit_list:
                print(f"\t{option} - {sit.replace(".csv","")}")
                option += 1

            print("\te - exit\n")
            choice = input("choice: ")


            if choice == 'e': break

            elif choice.isdigit():
                try:
                    choice = int(choice)
                    if choice >= 0 or choice < len(sit_list):
                        self.gen_question(sit_list[int(choice)])

                except Exception as e:
                    print(f"Something went wrong!\n error: {e}")
    

    def get_relationship(self, relationship):

        match relationship:

            case 1:
                return "Total Stranger"
            case 2:
                return "Acquaintance"
            case 3:
                return "Friend"
            case 4:
                return "Loved One"

    def get_social_status(self, status):

        match status:

            case 1:
                return "Murderer"
            case 2:
                return "Thief"
            case 3:
                return "Average Joe"
            case 4:
                return "Upstanding citizen"
            case 5:
                return "Doctor"

    def get_harm(self, harm):
        match harm:

            case 0:
                return "Slow and painful Death"
            case 1:
                return "Instant Death"


    def print_prompt(self,
                     num_on_main,
                     num_on_alt,
                     relationship_main,
                     relationship_alt,
                     harm_severity_main,
                     harm_severity_alt,
                     social_pressure,
                     social_importance_main,
                     social_importance_alt):
        print("\n\nYour trolley problem:\n")
        print(f'''Status of main rail:\n
              Number of people: {num_on_main}
              Relationship to them: {self.get_relationship(relationship_main)}
              Group Social status: {self.get_social_status(social_importance_main)}
              Harm on collision: {self.get_harm(harm_severity_main)}''')
        print("\n")
        print(f'''Status of alternate rail:\n
              Number of people: {num_on_alt}
              Relationship to them: {self.get_relationship(relationship_alt)}
              Group Social status: {self.get_social_status(social_importance_alt)}
              Harm on collision: {self.get_harm(harm_severity_alt)}''')
        print("\n")

        match social_pressure:
            case 0:
                print("Nobody is watching you make this choice.")
            case 1:
                print("There are people watching you make this choice.")
        print("\n\n")

    def build_quesiton(self):
            os.system('clear')
            print("Please ONLY enter integers for the following questions!\n")
            try:
                num_on_main = int(input("How many people are on the main rail?: "))
                num_on_alt = int(input("How many people are on the alternate rail?: "))
                print('''
                Notes:
                    1 - Total Stranger
                    2 - Acquaintance
                    3 - Friend
                    4 - Loved One
                
                Going above or below limits may cause unexpected results
                      ''')
                relationship_main = int(input("What is your relationship to the people on main rail?: "))
                relationship_alt = int(input("What is your relationship to the people on alternate rail?: "))
                
                print('''
                Notes:
                    0 - suffer slowly
                    1 - instant death
                
                Going above or below limits may cause unexpected results
                      ''')
                
                harm_severity_main = int(input("How harsh will impact be on the main rail?: "))
                harm_severity_alt = int(input("How harsh will impact be on the alternate rail?: "))
                print('''
                Notes:
                    0 - No
                    1 - Yes
                
                Going above or below limits may cause unexpected results
                      ''')
                social_pressure = int(input("Are people watching? "))
                print('''
                Notes:
                    1 - Murderer
                    2 - Thief
                    3 - Average Joe (Neutral person)
                    4 - Upstanding Citizen (Donates to charity, Holds doors open for people, etc.)
                    5 - Doctor
                Going above or below limits may cause unexpected results
                ''')
                social_importance_main = int(input("How do the people on the main rail impact society?: "))
                social_importance_alt = int(input("How do the people on the alternate rail impact society?: "))
        
                problem_name = input("Name this trolley problem: ") + ".csv"

                ##turn inputs into csv file
                d = {
                'num_on_main':[num_on_main],
                'num_on_alt':[num_on_alt],
                'relationship_main':[relationship_main],
                'relationship_alt':[relationship_alt],
                'harm_severity_main':[harm_severity_main],
                'harm_severity_alt':[harm_severity_alt],
                'social_pressure':[social_pressure],
                'social_importance_main':[social_importance_main],
                'social_importance_alt':[social_importance_alt]}
                
                df = pd.DataFrame(d)

                df.to_csv("situations/"+problem_name)

            except Exception as e:

                print(e)

            
    

    def gen_question(self,csv=None):

        ## if there is no CSV we need to randomly create a trolley problem
        if csv == None:

            ##Number of people on rails
            num_on_alt = random.choice(range(1, 5))
            num_on_main = random.choice(range(1, 5))

            ##Relationships - ]
            # 1 - stranger 
            # 4 - loved one
            relationship_main = random.choice(range(1, 5))
            relationship_alt = random.choice(range(1, 5))

            ##Harm 
            # 0 - suffer slowly
            # 1 - instant death

            harm_severity_main = random.choice([0, 1])
            harm_severity_alt = random.choice([0, 1])

            ##Is there pressure?
            social_pressure = random.choice([0, 1])

            ##Societal importance 
            # 1 = thief 
            # 5 = doctor

            social_importance_main = random.choice(range(1, 6))
            social_importance_alt = random.choice(range(1, 6))
        
        else:

            df = pd.read_csv("situations/"+csv)
            num_on_main = df.loc[0,'num_on_main']
            num_on_alt = df.loc[0,'num_on_alt']
            relationship_main = df.loc[0,'relationship_main'] 
            relationship_alt = df.loc[0,'relationship_alt']
            harm_severity_main = df.loc[0,'harm_severity_main']
            harm_severity_alt = df.loc[0,'harm_severity_alt']
            social_pressure = df.loc[0,'social_pressure']
            social_importance_main = df.loc[0,'social_importance_main']
            social_importance_alt = df.loc[0,'social_importance_alt']

            os.system('clear')

            print(f"successfully loaded {csv.replace('.csv','')} trolley problem!")

            
            

        if not self.hide: self.print_prompt(
                          num_on_main,
                          num_on_alt,
                          relationship_main,
                          relationship_alt,
                          harm_severity_main,
                          harm_severity_alt,
                          social_pressure,
                          social_importance_main,
                          social_importance_alt)
        ##get user input

        if self.invterviewee == 'h':
            need_response = True
            while need_response:
                print("What would you do? (y/n)")
                decision = input()
                if decision == 1 or decision.lower() == "yes" or decision.lower() == "y" or decision.lower() == 'pull':
                    decision = 1
                    break
                elif decision == 0 or decision.lower() == "no" or decision.lower() == "n":
                    decision = 0
                    break

                else:
                    print("Invalid answer!")
            print("----------------------------------------")

        else:
            if not self.hide: print("The AI is in control on this problem...\n\n")
            if not self.hide: input("--- PRESS 'ENTER' TO SEE RESULT ---\n\n\n")
            decision = self.model.predict([num_on_main,
                num_on_alt,
                relationship_main,
                relationship_alt,
                harm_severity_main,
                harm_severity_alt,
                social_pressure,
                social_importance_main,
                social_importance_alt])[0]
            
            if decision:
                if not self.hide: 
                    f = open("ascii_art/lever.txt",'r')
                    file_contents = f.read()
                    print(file_contents)
                    f.close()

                    print("\nThe AI pulled the lever!")
            else: 
                if not self.hide:
                    f = open("ascii_art/coffeecup.txt",'r')
                    file_contents = f.read()
                    print(file_contents)
                    f.close()
            
                    print("\nThe AI did nothing...")
            
            if not self.hide: print("\n\n")
            if not self.hide: input("--- PRESS 'ENTER' TO RETURN TO MENU ---\n\n\n")
            

        return [num_on_main,
                num_on_alt,
                relationship_main,
                relationship_alt,
                harm_severity_main,
                harm_severity_alt,
                social_pressure,
                social_importance_main,
                social_importance_alt,
                decision]


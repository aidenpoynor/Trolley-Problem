import random


class Survey:

    def __init__(self, quant_questions=1):

        self.info = []

        for question in range(0,quant_questions):
            self.info.append(self.gen_question())

    def get_relationship(self, relationship):

        match relationship:

            case 1:
                return "Total Stranger"
            case 2:
                return "Acquaintance"
            case 3:
                return "Friend"
            case _:
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
            case _:
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
                print("There is no pressure for you to pull the lever")
            case 1:
                print("There is a lot of pressure for you to pull the lever!")

    def gen_question(self):

        ##Number of people on rails
        num_on_alt = random.choice(range(1, 5))
        num_on_main = random.choice(range(1, 5))

        ##Relationships - ]
        # 1 - stranger 
        # 4 - loved one
        relationship_main = random.choice(range(1, 4))
        relationship_alt = random.choice(range(1, 4))

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

        social_importance_main = random.choice(range(1, 5))
        social_importance_alt = random.choice(range(1, 5))

        self.print_prompt(
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


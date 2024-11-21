from survey import Survey
import pandas as pd

def get_relationship(relationship):

    match relationship:

        case 1:
            return "Total Stranger"
        case 2:
            return "Acquaintance"
        case 3:
            return "Friend"
        case _:
            return "Loved One"

def get_social_status(status):

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

def get_harm(harm):
    match harm:

        case 0:
            return "Slow and painful Death"
        case _:
            return "Instant Death"

def run_analysis(model):
    data = []
    questions = 100
    surv_data = Survey(100,'c',model,True)

    df = pd.DataFrame(surv_data.info,columns=surv_data.classes)
    print(df.head(10))

    print(f"Number of times lever was pulled: {df['decision'].sum()}")

    pulled = df[df["decision"]==1]
    not_pulled = df[df["decision"]==0]

    print(f"Number of people killed: {pulled['num_on_alt'].sum()+not_pulled['num_on_main'].sum()}")
    print(f"Number of people spared: {pulled['num_on_main'].sum()+not_pulled['num_on_alt'].sum()}")

    # Add columns for saved and killed social statuses based on decisions
    df['saved_social_status'] = df.apply(
        lambda row: row['social_importance_main'] if row['decision'] == 1 else row['social_importance_alt'], axis=1
    )

    df['killed_social_status'] = df.apply(
        lambda row: row['social_importance_alt'] if row['decision'] == 1 else row['social_importance_main'], axis=1
    )

    # Analyze the most common social statuses saved and killed
    saved_counts = df['saved_social_status'].value_counts()
    killed_counts = df['killed_social_status'].value_counts()

    most_common_saved = saved_counts.idxmax()
    most_common_killed = killed_counts.idxmax()

    print("Most common social status of people saved:", get_social_status(most_common_saved))
    print("Most common social status of people killed:", get_social_status(most_common_killed))


    # Add columns for saved and killed social statuses based on decisions
    df['saved_relationship_status'] = df.apply(
        lambda row: row['relationship_main'] if row['decision'] == 1 else row['relationship_alt'], axis=1
    )

    df['killed_relationship_status'] = df.apply(
        lambda row: row['relationship_alt'] if row['decision'] == 1 else row['relationship_main'], axis=1
    )

    # Analyze the most common social statuses saved and killed
    saved_counts = df['saved_social_status'].value_counts()
    killed_counts = df['killed_social_status'].value_counts()

    most_common_saved = saved_counts.idxmax()
    most_common_killed = killed_counts.idxmax()

    print("Most common relationship status of people saved:", get_relationship(most_common_saved))
    print("Most common relationship status of people killed:", get_relationship(most_common_killed))



    #print(f"Social status of majority saved")
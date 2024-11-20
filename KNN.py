from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
class KNN:

    def __init__(self,data):
        print("Building KNN")
        self.data = pd.read_csv(data)

        print(self.data.head(10))
        self.knn = KNeighborsClassifier(n_neighbors=3)

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
        
        X = self.data.drop("decision", axis=1)  # Drop the target column
        y = self.data["decision"]  # Select the target column

        self.knn.fit(X,y)
    

    def predict(self,predict_data):
        predict = self.knn.predict(predict_data)
        return predict
    

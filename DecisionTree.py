from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import precision_score, recall_score, f1_score
from IPython.display import SVG, display
import pandas as pd
from graphviz import Source
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure



class DecisionTree:

    def __init__(self,data):

        print("Building a Decision Tree model...")

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

        self.data = pd.read_csv(data)
        X = self.data.drop("decision", axis=1)  # Drop the target column
        y = self.data["decision"]  # Select the target column

        

        self.treeclf = DecisionTreeClassifier(max_depth=3, random_state=1)
        
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27)

        # Train the classifier on the training data
        self.treeclf.fit(X_train, y_train)

        # Predict on the testing data
        y_pred = self.treeclf.predict(X_test)

        # Calculate precision, recall, and F-score
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f_score = f1_score(y_test, y_pred)

        print("Precision:", precision)
        print("Recall:", recall)
        print("F-score:", f_score)

    def predict(self, predict_data):
        self.classes = ["num_on_main",
                        "num_on_alt",
                        "relationship_main",
                        "relationship_alt",
                        "harm_severity_main",
                        "harm_severity_alt",
                        "social_pressure",
                        "social_importance_main",
                        "social_importance_alt"]
        
        predict = pd.DataFrame([predict_data], columns=self.classes)
        prediction = self.treeclf.predict(predict)

        #TODO: fix prediction point stuff
        #self.visualize(predict_data)
        return prediction
    
    def visualize(self, predict_data=None):
        """
        Visualize the data in 2D using PCA and optionally plot the prediction point.
        """

        self.features_names = ["People on main",
                        "People on alt",
                        "relationship on main",
                        "relationship on alt",
                        "Harm on main",
                        "Harm on alt",
                        "Social pressure?",
                        "Social status on main",
                        "social status on alt"]
        
        
        

        # Visualize the tree
        plt.figure(figsize=(12, 8))
        plot_tree(self.treeclf, filled=True, feature_names=self.classes, class_names=["not pulled","pulled"])
        plt.show()

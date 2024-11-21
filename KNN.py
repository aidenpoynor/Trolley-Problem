import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

class KNN:

    def __init__(self, data):
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

        self.X = X
        self.y = y
        self.knn.fit(X, y)
    

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
        prediction = self.knn.predict(predict)
        #TODO: fix prediction point stuff
        #self.visualize(predict_data)
        return prediction
    
    def visualize(self, predict_data=None):
        """
        Visualize the data in 2D using PCA and optionally plot the prediction point.
        """
        # Perform PCA for dimensionality reduction
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(self.X)

        # Map target labels to colors
        colors = ['red', 'blue']
        target_colors = [colors[label] for label in self.y]

        # Plot the data points
        plt.figure(figsize=(10, 7))
        for i, color in enumerate(colors):
            plt.scatter(X_pca[self.y == i, 0], X_pca[self.y == i, 1], 
                        label=f"Class {i}", c=color, alpha=0.6)
        
        # Plot the prediction point if provided
        if predict_data is not None:
            predict_pca = pca.transform([predict_data])
            predicted_class = self.predict(predict_data)[0]
            plt.scatter(predict_pca[0, 0], predict_pca[0, 1], 
                        c=colors[predicted_class], edgecolor='k', s=100, 
                        label=f"Prediction (Class {predicted_class})", marker='X')

        plt.title("KNN Data Visualization (PCA Reduced)")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.legend()
        plt.savefig("AI_Visualization_KNN.png")
        plt.cla()

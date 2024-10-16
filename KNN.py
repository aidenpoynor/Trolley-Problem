from sklearn.neighbors import KNeighborsClassifier

class KNN:

    def __init__(self,data):
        print("Building KNN")
        self.data = data

        self.knn = KNeighborsClassifier(n_neighbors=1)

        self.classes = ["Adults","Kids"]
        self.knn.fit(self.data, self.classes)
    

    def predict(self,predict_data):
        predict = self.knn.predict(predict_data)
        return predict
    

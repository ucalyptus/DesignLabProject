import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib
from joblib import dump, load


import sys
sys.path.append('../')

class Trainer ():
    def __init__(self,df) :
        self.TrainingDataSet = df
       
    def callExtractor(self):
        return Extractor(self.TrainingDataSet)
        
    def train_gini_decision_fit(self,X,y) :
        X_train,_,y_train,_ = train_test_split(X,y,test_size=0.2,random_state=10)
        classifier = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=5, min_samples_leaf=5)
        classifier.fit(X_train,y_train)
        return classifier 
        
class Extractor():
    def __init__(self,ExtractData):
        self.ExtractData = ExtractData
    
    def FeatureExtraction(self,ExtractData):
        df = ExtractData
        df.card.replace(['yes','no'], ['1', '0'], inplace=True)
        X=df[["reports","expenditure","age","income"]]
        y=df["card"]
        return X,y



if __name__ == '__main__':
    df  = pd.read_csv('dataset.csv')
    tt = Trainer(df)
    exc = tt.callExtractor()
    X,y = exc.FeatureExtraction(df)
    clf = tt.train_gini_decision_fit(X,y)
    dump(clf, 'model.joblib') 
    
    

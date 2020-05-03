from future import print_function
from future import division
import pandas as pd
import joblib
import requests
import sklearn
import sys
sys.path.append('../')

class Extractor():
    def __init__(self,features):
        self.features = features
    def FeatureExtraction(df):
        return df[self.features]
        
class Predictor():
    def __init__(self,path,model_path):
        self.datapath = path
        self.model_path = model_path
    def getSanitizedApplicationData():
        return pd.read_csv(self.datapath)
    def callExtractor(settings):
        return Extractor(settings)
    def model_load():
        return joblib.load(self.model_path)
    def prediction_function(df,model):
        return model.predict(df)

if __init__ == '__main__':
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True)
    open('model.joblib', 'wb').write(r.content)
    pred = Predictor('SanitizedApplication.csv','model.joblib')
    features = ['reports','expenditure','active','income']
    df = pred.getSanitizedApplicationData()
    exc = pred.callExtractor(features)
    df = exc.FeatureExtraction(df)
    Model = pred.model_load()
    out = pred.prediction_function(df,Model)

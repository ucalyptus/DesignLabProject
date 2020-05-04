from future import print_function
from future import division
import pandas as pd
import joblib
import requests
import sklearn
import sys
import sklearn.util.random as rnd
sys.path.append('../')

class Extractor():
    def __init__(self,features):
        self.features = features
    def FeatureExtraction(df):
        return df[self.features]
        
class Predictor():
    def __init__(self,path,modelfile):
        self.datapath = path
        self.modelfile = modelfile
    def getSanitizedApplicationData():
        return pd.read_csv(self.datapath)
    def callExtractor(settings):
        return Extractor(settings)
    def model_load():
        return joblib.load(self.modelfile)
    def prediction_function(df,model):
        card = np.asarray(len(df))
        card = model.predict(df)
        return card


if __init__ == '__main__':
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    open('model.joblib', 'wb').write(r.content) #saves it as so
    pred = Predictor('SanitizedApplication.csv','model.joblib')
    features = ['reports','expenditure','active','income']
    df = pred.getSanitizedApplicationData()
    exc = pred.callExtractor(features)
    df = exc.FeatureExtraction(df)
    Model = pred.model_load()
    card = pred.prediction_function(df,Model)
    id = rnd.sample_without_replacement(n_population=1000,n_samples=df.shape[0],method="reservoir_sampling")
    df.insert(0,'ApplicationId',id)
    df.insert(1,'Status',card)
    df.to_csv('unapproved_prediction.csv', index=False)

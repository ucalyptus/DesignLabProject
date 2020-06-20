# coding: utf-8

"""

@Author: Sayantan Das
@Github: ucalyptus

"""

import pandas as pd
import joblib
import requests
import sklearn
import sys
import sklearn.utils.random as rnd
import numpy as np
sys.path.append('../')

class Extractor():
    def __init__(self,features):
        self.features = features
    def FeatureExtraction(self,df):
        return df[self.features]
        
class Predictor():
    def __init__(self,path,modelfile):
        self.datapath = path
        self.modelfile = modelfile
    def getSanitizedApplicationData(self):
        return pd.read_csv(self.datapath)
    def callExtractor(self,settings):
        return Extractor(settings)
    def model_load(self):
        return joblib.load(self.modelfile)
    def prediction_function(self,df,model):
        card = np.asarray(len(df))
        card = model.predict(df)
        return card


if __name__ == '__main__':
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
    df = pd.read_csv("application.csv", usecols = ['ApplicationId'])
    #id = rnd.sample_without_replacement(n_population=1400,n_samples=df.shape[0],method="reservoir_sampling")
    #df.insert(0,'ApplicationId',id)
    df.insert(1,'Status',card)
    df.to_csv('unapproved_prediction.csv', index=False)

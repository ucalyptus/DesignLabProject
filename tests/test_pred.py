import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
import sklearn
import sys
import requests
sys.path.append('../')
from src import pred
import os
import tracemalloc

tracemalloc.start()

class TestPrediction(unittest.TestCase):
  
  def test_features(self):
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    f=open('../tests/model.joblib', 'wb')
    f.write(r.content) #saves it as so
    f.close()
    ob = pred.Predictor('../src/SanitizedApplication.csv','model.joblib')
    features = pd.Index(['reports','expenditure','active','income'],dtype='object')
    df = ob.getSanitizedApplicationData()
    exc = ob.callExtractor(features)
    df = exc.FeatureExtraction(df)
    #df = pd.read_csv('../tests/prediction_attributes_1.csv')
    self.assertEqual(type(features),type(df.columns))
    
  def test_modelclass(self):
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    f = open('../tests/model.joblib', 'wb')
    f.write(r.content) #saves it as so
    f.close()
    ob = pred.Predictor('../src/SanitizedApplication.csv','../src/model.joblib')
    Model = ob.model_load()
    assert(type(Model) == sklearn.ensemble._forest.RandomForestClassifier)
    
  def test_expectedOutput(self):
    df = pd.read_csv('../src/unapproved_prediction.csv')
    dframe = pd.read_csv('../tests/ExpectedPrediction.csv')
    boolean = df.equals(dframe)
    self.assertTrue(boolean, "Wrong Prediction")
    
  def test_salary(self):
    df = pd.read_csv('../src/SanitizedApplication.csv')
    boolean = (df['income'] > 1.5).all()
    self.assertTrue(boolean, "Invalid Salary")
 
    
    
    
    

if __name__ == '__main__':
  unittest.main()
    
    
    
    
    

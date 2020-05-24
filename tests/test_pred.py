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
    open('../tests/model.joblib', 'wb').write(r.content) #saves it as so
    ob = pred.Predictor('../src/SanitizedApplication.csv','model.joblib')
    features = pd.Index(['reports','expenditure','active','income'],dtype='object')
    df = ob.getSanitizedApplicationData()
    exc = ob.callExtractor(features)
    df = exc.FeatureExtraction(df)
    self.assertEqual(type(features),type(df.columns))
    
  def test_modelclass(self):
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    open('../tests/model.joblib', 'wb').write(r.content) #saves it as so
    ob = pred.Predictor('../src/SanitizedApplication.csv','../src/model.joblib')
    Model = ob.model_load()
    assert(type(Model) == sklearn.ensemble._forest.RandomForestClassifier)
    
    
    

if __name__ == '__main__':
  unittest.main()
    
    
    
    
    

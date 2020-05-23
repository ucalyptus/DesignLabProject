import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
import sklearn
import sys
sys.path.append('../')
from src import pred
import os

class TestPrediction(unittest.TestCase):
  
  def Test_features(self):
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    open('model.joblib', 'wb').write(r.content) #saves it as so
    ob = pred.Predictor('SanitizedApplication.csv','model.joblib')
    features = pd.Index(['reports','expenditure','active','income'],dtype='object')
    df = ob.getSanitizedApplicationData()
    exc = ob.callExtractor(features)
    df = exc.FeatureExtraction(df)
    assert_equal(type(features),type(df.columns))
    
  def Test_modelclass(self):
    url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
    r = requests.get(url, allow_redirects=True) #downloads the file
    open('model.joblib', 'wb').write(r.content) #saves it as so
    ob = pred.Predictor('SanitizedApplication.csv','model.joblib')
    Model = ob.model_load()
    assert(type(Model) == sklearn.ensemble._forest.RandomForestClassifier)
    
    
    
    
    
    
    
    
    

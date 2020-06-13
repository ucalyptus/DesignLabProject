import pandas as pd
import unittest
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
import sklearn
import sys
sys.path.append('../')
from src import pred
import os
import tracemalloc
import requests
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
    self.assertEqual(type(features),type(df.columns))
    
  def test_modelclass(self):
    ob = pred.Predictor('../src/SanitizedApplication.csv','../src/model.joblib')
    Model = ob.model_load()
    self.assertEqual(type(Model), sklearn.ensemble._forest.RandomForestClassifier)
    
  def test_expectedOutput(self):

    df1 = pd.read_csv('../src/unapproved_prediction.csv')
    df2 = pd.read_csv('../tests/ExpectedPrediction.csv')
    df=df1.merge(df2,how='outer',indicator=True).loc[lambda x:x['_merge']=='right_only']
    dfr=df.count()
    dfr=list(dfr)
    correct_pred= 250 - dfr[1]
    acc=correct_pred/250
    if(acc>=0.8):
        boolean=True
    else:
        boolean=False
    
    self.assertTrue(boolean, "Wrong Prediction")
    
    
  def test_salary(self):
    df = pd.read_csv('../src/SanitizedApplication.csv')
    boolean = (df['income'] > 1.2).all()
    self.assertTrue(boolean, "Invalid Salary")


if __name__ == '__main__':
  unittest.main()
    
    
    
    
    

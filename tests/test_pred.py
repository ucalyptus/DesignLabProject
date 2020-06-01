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
    """url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
                r = requests.get(url, allow_redirects=True) #downloads the file
                f=open('../tests/model.joblib', 'wb')
                f.write(r.content) #saves it as so
                f.close()"""
    ob = pred.Predictor('../src/SanitizedApplication.csv','../src/model.joblib')
    features = pd.Index(['reports','expenditure','active','income'],dtype='object')
    #df = ob.getSanitizedApplicationData()
    #exc = ob.callExtractor(features)
    #df = exc.FeatureExtraction(df)
    df = pd.read_csv('../tests/prediction_attributes_1.csv')
    self.assertEqual(type(features),type(df.columns))
    
  def test_modelclass(self):
    """url = 'https://raw.githubusercontent.com/ucalyptus/scikit-on-gRPC/master/model.joblib'
                r = requests.get(url, allow_redirects=True) #downloads the file
                f = open('../tests/model.joblib', 'wb')
                f.write(r.content) #saves it as so
                f.close()"""
    ob = pred.Predictor('../src/SanitizedApplication.csv','../src/model.joblib')
    Model = ob.model_load()
    assert(type(Model) == sklearn.ensemble._forest.RandomForestClassifier)
    
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
    #boolean = df.equals(dframe)
    self.assertTrue(boolean, "Wrong Prediction")
    
    #Boolean_Check
    #import pandas as pd
    #import numpy as np
    #df1=pd.read_csv("unapproved_prediction.csv")
    #df2=pd.read_csv("ExpectedPrediction.csv")
    #col1=df1['Status'].tolist()
    #cola=df1['ApplicationId'].tolist()
    #col2=df2['Status'].tolist()
    #colb=df1['ApplicationId'].tolist()
    #col1=np.array(col1)
    #cola=np.array(cola)
    #col2=np.array(col2)
    #colb=np.array(colb)
    #r=np.array_equal(col1,col2)
    #r1=np.array_equal(cola,colb)
    #print(r)
    #print(r1)
    
    
  def test_salary(self):
    df = pd.read_csv('../src/SanitizedApplication.csv')
    boolean = (df['income'] >= 1.2).all()
    self.assertTrue(boolean, "Invalid Salary")
 
    
    
    
    

if __name__ == '__main__':
  unittest.main()
    
    
    
    
    

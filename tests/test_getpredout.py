import pandas as pd
import pandas.testing as pt
import pytest
import unittest
import sys
sys.path.append('../')
from src import getpredout
import os

class TestGetPredOut(unittest.TestCase):
  
  def test_attribs(self):
    df = pd.read_csv('../src/unapproved_prediction.csv')
    if('ApplicationId' in df.columns and 'Status' in df.columns):
      boolean = True
    self.assertTrue(boolean, 'Necessary attribute(s) missing')
    
    
  
  def test_categorical(self):
    df = pd.read_csv('../tests/categorical_values.csv')
    assert 'Yes' or 'No' in df.Status.values , "Only yes/no allowed" 
    if (not(df['Status'].str.contains('Yes')).any() or not(df['Status'].str.contains('No')).any()):
      boolean = False
    else:
      boolean = True
    
    self.assertTrue(boolean, "only yes/no permitted")

  def test_checkNull(self):
    df = pd.read_csv('../src/prediction.csv')

    b = df.isnull().any().any()
    self.assertFalse(b,"Null Values invalid ")
    
      

if __name__ == '__main__':
    unittest.main()
    
    
    
    

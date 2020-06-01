import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
sys.path.append('../')
from src import getpredout
import os

class TestGetPredOut(unittest.TestCase):
  
  def test_attribs(self):
    df = pd.read_csv('../src/unapproved_prediction.csv')
    if('ApplicationId' in df.columns and 'Status' in df.columns):
      boolean = true
    self.assertTrue(boolean, 'Necessary attribute(s) missing')
    
    
  
  def test_categorical(self):
    df = pd.read_csv('../src/prediction.csv')
    #assert 'Yes' or 'No' in df.Status.values , "Only yes/no allowed" 
    for status in df['Status']:
      if ((status != 'Yes') or (status =! 'No')):
        boolean = False
        break
      else:
        boolean = True
      
    self.assertTrue(boolean, "only yes/no permitted")
      
    b = df.isnull().any().any()
    self.assertFalse(b,"Null Values invalid ")
    
      

if __name__ == '__main__':
    unittest.main()
    
    
    
    

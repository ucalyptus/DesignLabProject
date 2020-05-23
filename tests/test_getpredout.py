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
  
  def Test_attribs(self):
    df = pd.read_csv('../unapproved_prediction.csv')
    assert('ApplicationId' in df.columns , "Invalid! Application Id mandatory ")
    assert('Status' in df.columns , "Invalid! Status mandatory ")
    
  
  def Test_categorical(self):
    df = pd.read_csv('../unapproved_prediction.csv')
    assert('Yes' or 'No' in df.Status.values , "Only yes/no allowed")
    b = df.isnull().any().any()
    self.assertFalse(b,"Null Values invalid ")

    
    
    
    
    
    

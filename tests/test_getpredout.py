import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import getpredout
import os

class TestGetPredOut(unittest.TestCase):
  
  def Test_attribs(self):
    df = pd.read_csv('unapproved_prediction.csv')
    assert('ApplicationId' in df.columns)
    assert('Status' in df.columns)
    
  
  def Test_categorical(self):
    df = pd.read_csv('unapproved_prediction.csv')
    
    
    
    
    

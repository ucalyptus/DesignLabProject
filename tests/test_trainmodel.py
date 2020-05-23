import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
sys.path.append('../')
from src import trainmodel
import os

class TestTrainModel(unittest.TestCase):
  
  def Test_traindb(self):
    df  = pd.read_csv('dataset.csv')
    assert_equal(df,pd.DataFrame, "Invalid")
    
    
    
    

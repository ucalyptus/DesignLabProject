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
  
  def test_traindb(self):
    df  = pd.read_csv('../src/dataset.csv')
    self.assertEqual(type(df),pd.DataFrame, "Invalid")
    
     def test_validAgeRange(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication(url)
    booleam = df["age"].between(20, 65, inclusive = True).all()
    self.assertTrue(boolean, "invalid age")
    
if __name__ == "__main__":
  unittest.main()

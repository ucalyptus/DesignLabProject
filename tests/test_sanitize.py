import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
sys.path.append('../')
from src import sanitize,ServerAPI


class TestSanitize(unittest.TestCase):
  
  def Test_getapplication(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication()
    assert_equal(df,pd.DataFrame,"Invalid Type")
    
  def Test_columns(self):
    obje = sanitize.Sanitizer()
    df = obje.getApplication()
    columns = list(df.columns)
    try:
      df_req = df[['reports', 'expenditure', 'active', 'income', 'ApplicationId']]
    except e:
      print("Invalid! All necessary columns not found :")
      print(e)
    unique_ids = set(df['ApplicationId'])
    assert len(df['ApplicationId']) == len(unique_ids) , "Invalid! All IDs are not unique"
    assert sum(df.isnull().sum()) == 0, "Null values found"
    



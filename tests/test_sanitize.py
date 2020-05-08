import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest

import sanitize


class TestSanitize(unittest.TestCase):
  
  def Test_getapplication(self):
    obje = sanitize.Sanitizer('https://raw.githubusercontent.com/ucalyptus/Double-Branch-Dual-Attention-Mechanism-Network/master/UP.csv')
    df = obje.getApplication()
    assert_equal(df,pd.DataFrame)
  def Columns(self, path_to_csv):
    df = pd.read_csv(path_to_csv)
    columns = list(df.columns)
    try:
      df_req = df[['reports', 'expenditure', 'active', 'income', 'ApplicationId']]
    except e:
      print("All necessary columns not found :")
      print(e)
    unique_ids = set(df['ApplicationId'])
    assert len(df['ApplicationId']) == len(unique_ids) , "All IDs are not unique"
    assert sum(df.isnull().sum()) == 0, "Null values found"
    



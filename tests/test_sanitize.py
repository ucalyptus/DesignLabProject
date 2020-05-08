import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest

import sanitize


class TestSanitize(unittest.TestCase):
  
  def Test_getapplication(self):
    obje = sanitize.Sanitizer('https://gist.githubusercontent.com/ucalyptus/fb8cb8605d38eea3653345340029660f/raw/583d28c165d822213278ca3da17e181ab41443b6/application.csv')
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
    



import pandas as pd
import pandas.testing as pt
import pytest
import pandas as pd
import unittest
import sys
sys.path.insert(0,r'/home/ucalyptus/DesignLabProject/')
import sanitize


class TestSanitize(unittest.TestCase):
  
  def Test_getapplication(self):
    
    obje = sanitize.Sanitizer('https://raw.githubusercontent.com/ucalyptus/Double-Branch-Dual-Attention-Mechanism-Network/master/UP.csv')
    df = obje.getApplication()
    assert_equal(df,pd.DataFrame)
    
    
    



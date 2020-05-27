import pandas as pd
import sys
sys.path.append('../')
from src import ServerAPI
from datetime import datetime

def check(element):
	if element == 1:
		return 'Yes'
	else:
		 return 'No'

def setApprovalPrediction(df):
  df['Status'] = df['Status'].apply(check)
  now = datetime.now()
  date_time = now.strftime("_%d-%m-%Y_%H:%M:%S")
  df.to_csv('prediction{}.csv'.format(date_time), index=False)
  return df 

if __name__ == "__main__":
    df = pd.read_csv('../src/unapproved_prediction.csv')
    df = setApprovalPrediction(df)
    ServerAPI.upload()



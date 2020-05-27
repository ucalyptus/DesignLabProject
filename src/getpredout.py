import pandas as pd
import sys
sys.path.append('../')
from src import ServerAPI

def check(element):
	if element == 1:
		return 'Yes'
	else:
		 return 'No'

def setApprovalPrediction(df):
  #df = df.drop(feat_cols,axis=1)
  df['Status'] = df['Status'].apply(check)
  df.to_csv('prediction.csv', index=False)
  return df 

if __name__ == "__main__":
    feat_cols = ['reports','expenditure','active','income']
    df = pd.read_csv('../src/unapproved_prediction.csv')
    df = setApprovalPrediction(df)
    ServerAPI.upload()



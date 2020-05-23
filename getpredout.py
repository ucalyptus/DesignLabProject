import ftplib
import pandas as pd
import sys
sys.path.append('../')

def check(element):
	if element == '1':
		return 'Yes'
	else:
		 return 'No'

def setApprovalPrediction(df):
  df['Status'] = df['Status'].apply(check)
  df = df.drop(feat_cols,axis=1)
  df.to_csv('prediction.csv', index=False)
  
feat_cols = ['reports','expenditure','age','income']
df = pd.read_csv('unapproved_prediction.csv')
setApprovalPrediction(df)
import ServerAPI
ServerAPI.upload()



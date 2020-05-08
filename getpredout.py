import ftplib
import pandas as pd
from future import print_function
from future import division
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
session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')  #awaiting ftp server help from team
file = open('prediction.csv','rb')                  # file to send
session.storbinary('STOR prediction.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()



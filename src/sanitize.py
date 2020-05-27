import pandas as pd
import sys
sys.path.append('../')
import ftplib
from src import ServerAPI
class Sanitizer():
    def __init__(self):
        ServerAPI.download()
        
    
    def getApplication(self,url):
        self.ApplicationData = url
        return pd.read_csv(self.ApplicationData)

    
    def performSanitization(self):
        df = self.getApplication('application.csv')
        col_list = ["reports", "income", "active", "expenditure"]
        df = pd.read_csv("application.csv", usecols=col_list)
        return df

def getSanitizedApplicationData(obj):
    SanitizedApplicationData=obj.performSanitization()
    return SanitizedApplicationData


if  __name__ == "__main__":

    callsan = Sanitizer()
    df=getSanitizedApplicationData(callsan)
    df.to_csv('SanitizedApplication.csv')


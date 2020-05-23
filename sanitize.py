import pandas as pd
import sys
sys.path.append('../')
import ftplib
import ServerAPI
class Sanitizer():
    def __init__(self):
        ServerAPI.download()
        
    
    def getApplication(self,url):
        self.ApplicationData = url
        return pd.read_csv(self.ApplicationData)

    
    def performSanitization(self):
        df = self.getApplication('application.csv')
        return df

def getSanitizedApplicationData(obj):
    SanitizedApplicationData=obj.performSanitization()
    return SanitizedApplicationData


if  __name__ == "__main__":

    callsan = Sanitizer()
    df=getSanitizedApplicationData(callsan)
    df.to_csv('SanitizedApplication.csv')


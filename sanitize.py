import pandas as pd
import sys
sys.path.append('../')
import ftplib
import ServerAPI
class Sanitizer():
    def __init__(self):
        ServerAPI.download()
        
    def performSanitization():
        df = getApplication()
        
        return df
    def getApplication():
        return pd.read_csv(self.ApplicationData)


def getSanitizedApplicationData(obj):
    SanitizedApplicationData=obj.performSanitization()
    return SanitizedApplicationData


if  __init__ == "__main__":

    callsan = Sanitizer()
    df=getSanitizedApplicationData(callsan)
    df.to_csv('SanitizedApplication.csv')


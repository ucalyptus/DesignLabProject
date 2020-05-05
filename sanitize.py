import pandas as pd
#import ServerAPI as server_api
import sys
sys.path.append('../')

class Sanitizer():
    def __init__(self,bnk_url):
        pass
     #   self.ApplicationData = server_api.fetch_from(bnk_url)
    def performSanitization():
        df = getApplication()
        ## must think of doing some checks here
        return df
    def getApplication():
        return pd.read_csv(self.ApplicationData)


def getSanitizedApplicationData(obj):
    SanitizedApplicationData=obj.performSanitization()
    return SanitizedApplicationData


if  __init__ == "__main__":

    callsan = Sanitizer(bnk_url)
    df=getSanitizedApplicationData(callsan)
    df.to_csv('SanitizedApplication.csv')


import pandas as pd
import sys
sys.path.append('../')
import ftplib
class Sanitizer():
    def __init__(self,bnk_url):
        session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')
        file = open('application.csv','rb')
        session.retrbinary('RETR application.csv',file)
        file.close()
        session.quit()
     
    def performSanitization():
        df = getApplication()
        
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


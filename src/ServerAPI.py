import ftplib
url = 'ftp.drivehq.com'
username = 'MavenDev'
password = 'Teammaven123'

def download():
    session = ftplib.FTP(url,username,password)
    handle = open('application.csv','wb')
    session.retrbinary('RETR application.csv',handle.write)
    handle.close()
    session.quit()

def upload():
    session = ftplib.FTP(url,username,password)
    handle = open('prediction.csv','rb')
    session.storbinary('STOR prediction.csv',handle)
    handle.close()
    session.quit()

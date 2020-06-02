import ftplib
host = 'ftp.drivehq.com'
user = 'MavenDev'
passwd = 'Teammaven123'

def download():
    session = ftplib.FTP(host,user,passwd)
    handle = open('application.csv','wb')
    session.retrbinary('RETR application.csv',handle.write)
    handle.close()
    session.quit()

def upload():
    session = ftplib.FTP(host,user,passwd)
    handle = open('prediction.csv','rb')
    session.storbinary('STOR prediction.csv',handle)
    handle.close()
    session.quit()

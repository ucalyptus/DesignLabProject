import ftplib

def download():
    session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')
    fil = open('application.csv','rb')
    session.retrbinary('RETR application.csv',file)
    fil.close()
    session.quit()
def upload():
    
    session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')
    fil = open('prediction.csv','rb')
    session.storbinary('STOR prediction.csv',file)
    fil.close()
    session.quit()

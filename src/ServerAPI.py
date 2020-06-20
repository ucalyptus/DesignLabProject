# coding: utf-8

"""

@Author: Sayantan Das
@Github: ucalyptus

"""
import ftplib

def download():
    session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')
    handle = open('application.csv','wb')
    session.retrbinary('RETR application.csv',handle.write)
    handle.close()
    session.quit()
    print('Downloaded Successfully')

def upload():
    session = ftplib.FTP('ftp.drivehq.com','MavenDev','Teammaven123')
    fil = open('prediction.csv','rb')
    session.storbinary('STOR prediction.csv',fil)
    fil.close()
    session.quit()
    print('Uploaded Successfully')

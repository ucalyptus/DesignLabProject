# coding: utf-8

"""

@Author: Sayantan Das
@Github: ucalyptus

"""
import ftplib
from secrets import FTPID,FTPPWD

username = FTPID
password = FTPPWD

def download():
    session = ftplib.FTP('ftp.drivehq.com',username,password)
    handle = open('application.csv','wb')
    session.retrbinary('RETR application.csv',handle.write)
    handle.close()
    session.quit()
    print('Downloaded Successfully')

def upload():
    session = ftplib.FTP('ftp.drivehq.com',username,password)
    fil = open('prediction.csv','rb')
    session.storbinary('STOR prediction.csv',fil)
    fil.close()
    session.quit()
    print('Uploaded Successfully')

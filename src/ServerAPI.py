
import ftplib
from . import config

def download():
    session = ftplib.FTP(config.FTP_HOST, config.FTP_USER, config.FTP_PASS)
    if config.APPLICATION_DATA_FILE in session.nlst():
        handle = open(config.APPLICATION_DATA_FILE, 'wb')
        session.retrbinary(f'RETR {config.APPLICATION_DATA_FILE}', handle.write)
        handle.close()
        print('Downloaded Successfully')
    else:
        print(f'{config.APPLICATION_DATA_FILE} not found on the server.')
    session.quit()

def upload():
    session = ftplib.FTP(config.FTP_HOST, config.FTP_USER, config.FTP_PASS)
    if config.PREDICTIONS_FILE not in session.nlst():
        fil = open(config.PREDICTIONS_FILE, 'rb')
        session.storbinary(f'STOR {config.PREDICTIONS_FILE}', fil)
        fil.close()
        print('Uploaded Successfully')
    else:
        print(f'{config.PREDICTIONS_FILE} already exists on the server.')
    session.quit()


import ftplib
from . import config

def download():
    session = None
    try:
        session = ftplib.FTP(config.FTP_HOST, config.FTP_USER, config.FTP_PASS)
        if config.APPLICATION_DATA_FILE in session.nlst():
            with open(config.APPLICATION_DATA_FILE, 'wb') as handle:
                session.retrbinary(f'RETR {config.APPLICATION_DATA_FILE}', handle.write)
            print('Downloaded Successfully')
        else:
            print(f'{config.APPLICATION_DATA_FILE} not found on the server.')
    finally:
        if session:
            session.quit()

def upload():
    session = None
    try:
        session = ftplib.FTP(config.FTP_HOST, config.FTP_USER, config.FTP_PASS)
        if config.PREDICTIONS_FILE not in session.nlst():
            with open(config.PREDICTIONS_FILE, 'rb') as fil:
                session.storbinary(f'STOR {config.PREDICTIONS_FILE}', fil)
            print('Uploaded Successfully')
        else:
            print(f'{config.PREDICTIONS_FILE} already exists on the server.')
    finally:
        if session:
            session.quit()

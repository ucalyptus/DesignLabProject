import ftplib
import pandas as pd
from future import print_function
from future import division
import sys
sys.path.append('../')

df.to_csv('prediction.csv')


session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
file = open('prediction.csv','rb')                  # file to send
session.storbinary('STOR prediction.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()



import ftplib
import pandas as pd
from future import print_function
from future import division
import sys
sys.path.append('../')

### data is a list of lists like data=[['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns = ['ApplicationId', 'Status']) 
df.to_csv('prediction.csv')


session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
file = open('prediction.csv','rb')                  # file to send
session.storbinary('STOR prediction.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()



import ftplib
import unittest
host = 'ftp.drivehq.com'
user = 'MavenDev'
passwd = 'Teammaven123'

class TestFTP(unittest.TestCase):
	def test_connection(self):
	    session = ftplib.FTP(host,user,passwd)
	    print(session.getwelcome())
	    session.quit()


if __name__ == '__main__':
  unittest.main()

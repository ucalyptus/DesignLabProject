### Author: Muskan

# FTP SERVER

## TO VIEW IN BROWSER
* Copy & Paste the following link to your browser

        ftp://MavenDev:Teammaven123@ftp.drivehq.com/

## INSTALLATION GUIDE FOR THE FTP SERVER CLIENT
### FOR LINUX
* Open the terminal
* Run the following command:

        ftp -p ftp.drivehq.com

* Enter the **Username** and **Password** as asked
* After the connection has been established, view the files by typing the following command after **ftp>** to get the list 

        ls
* To close the connection, type the following command after **ftp>**

        bye
* **For help view image**

    ![](image3.png)

### FOR WINDOWS
* Install [WinSCP](https://winscp.net/eng/download.php) ftp client
* Open the client and start a new connection login

    ![](image1.png)

* In the Login window :
    * Set the **Hostname** as 
        ```bash
        ftp.drivehq.com
       ```

    * Set the **Port Number** at **21**

    * Enter the **Username** and **Password**


* Click on **Login** and the files on the server will be on the right side of the window. 

    ![](image2.png)

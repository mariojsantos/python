#!/usr/bin/python
#Script to put a file on FTP accessible directory 

import ftplib

session = ftplib.FTP()

host = "<target's ip >"

#ftp port num
port = 21

session.connect(host, port)

print (session.getwelcome())

session.login("User", "Password") 

file = open('filename','rb') # file to send

#Fills with the absolute path to the file
session.storbinary(r'STOR /home/example/filename', file) # send the file
file.close() # close file and FTP
session.quit()

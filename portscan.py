#!/usr/bin/python
import socket,sys

portas={21,23,80,443,139,445,2221,3389,5900,8080,8443}

for porta in portas:
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if meusocket.connect_ex((sys.argv[1],porta)) == 0:
        print "Porta ",porta,"[ABERTA]"
        meusocket.close()

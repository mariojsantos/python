#!/usr/bin/python
# A realy simple python portscan  
import socket,sys

#Selected ports
ports={21,23,80,443,139,445,2221,3389,5900,8080,8443}

for port in ports:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if mysocket.connect_ex((sys.argv[1],port)) == 0:
        print "Port ",port,"[OPEN]"
        mysocket.close()

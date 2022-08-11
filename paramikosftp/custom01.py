#!/usr/bin/env python3

import paramiko
import os
import getpass

def movethemfiles(destination):
    #make a sftp connection object called planetExpress and opens a connection
    with paramiko.SFTPClient.from_transport(destination) as planetExpress:
        for x in os.listdir("/home/student/filestocopy/"):
            if not os.path.isdir("/home/student/filestocopy/"+x):
                planetExpress.put("/home/student/filestocopy/"+x, "/tmp/"+x)
    destination.close()
def main():
#where to connect to
    destination = paramiko.Transport("10.10.2.3", 22)

##how to connect
    destination.connect(username="bender", password=getpass.getpass())
 
    movethemfiles(destination)

if __name__ == "__main__":
    main()


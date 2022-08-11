#!/usr/bin/env python3

import paramiko
import os
import getpass

def main():
#where to connect to
    destination = paramiko.Transport("10.10.2.3", 22)

##how to connect
    destination.connect(username="bender", password=getpass.getpass())

    #make an sftp connection object
          #module.class.method(argument)
    with paramiko.SFTPClient.from_transport(destination) as planetExpress:
        for x in os.listdir("/home/student/filestocopy/"):
            if not os.path.isdir("/home/student/filestocopy/"+x):
                planetExpress.put("/home/student/filestocopy/"+x, "/tmp/"+x)
    
    destination.close()

if __name__ == "__main__":
    main()


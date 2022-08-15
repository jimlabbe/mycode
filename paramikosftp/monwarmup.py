#!/usr/bin/env python3

import paramiko
import os
import getpass

def main():
#describe the connection data
everyone = [
        {'un': 'bender', 'ip':'10.10.2.3'},
        {'un': 'zoidberg', 'ip':'10.10.2.5'},
        {'un': 'fry', 'ip':'10.10.2.4'},
        ]

#harvest private key
mykey = paramiko.RSAKey.from_privae_key_file("/home/student/.ssh/id_rsa")

    #where to connect to
#    destination = paramiko.Transport("10.10.2.3", 22)
##how to connect
#    destination.connect(username="bender", password=getpass.getpass())

    #make an sftp connection object
          #module.class.method(argument)
    for everyone in everyone:
        sshsession = paramiko.SSHClient()

        #add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to... " + everyone.get("un") + "@" + everyone.get("ip"))

        #make a connection
        sshsession.connect(hostname=everyone.get("ip"), username=everyone.get("un"), pkey=mykey)
        #touch the file to each users home directory
        sshsession.exec_command("sudo apt install sl -y")

        #check if its installed
        sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "File exists" || echo "file does not exist"')

        #displayoutput
        resp= sessout.read().decode('utf-8')

        if "File exists" in resp:
            #appropriate action


#        with paramiko.SFTPClient.from_transport(destination) as planetExpress:
#        for x in os.listdir("/home/student/filestocopy/"):
#            if not os.path.isdir("/home/student/filestocopy/"+x):
#                planetExpress.put("/home/student/filestocopy/"+x, "/tmp/"+x)
    
#    destination.close()

if __name__ == "__main__":
    main()


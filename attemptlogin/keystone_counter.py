#!/usr/bin/env python3

loginfail = 0 # initialize counter for fails

#open file
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

#enter lines from file into memory as variable
keystone_file_lines = keystone_file.readlines()
keystone_file.close()


#loop over list of lines and increase counter for every matched pattern
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 

print("The number of failed log in attempts is", loginfail)


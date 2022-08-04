#!/usr/bin/env python3
'''For - looping across a file opened with 'with' while also being gentle on memory'''

# open file using with in read mode
with open("dnsservers.txt", "r") as dnsfile: #r means open in read mode
    #indent keeps the dnsfile object open

    # no need to create a list object here

    for svr in dnsfile: # loop over lines
        svr = svr.rstrip('/n')

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "/n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "/n")


#no need to close file, it closes automatically


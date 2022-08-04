#!/usr/bin/env python3

# open file using with in read mode
with open("dnsservers.txt", "r") as dnsfile:
    #indent keeps the dnsfile object open

    dnslist = dnsfile.readlines() # create a list of lines

    for svr in dnslist: # loop over lines
        print(svr, end="") # print and end without a newline

#no need to close file, it closes automatically


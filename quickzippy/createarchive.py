#!/usr/bin/env python3
import os
import zipfile

def zipdir(dirpath, zipfileobj):
    '''writes data into our zipfile'''
    #os.walk returns a 3-tuple
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            print(os.path.join(root,file)) #creates an absolute path
            zipfileobj.write(os.path.join(root, file)) # adds files to our zipfi
    return None

def main():
    #ask the user for dir to be archived
    dirpath = input("What directory are we archiving? ")

    #if dir exists, then begin archiving it
    if os.path.isdir(dirpath):
        zippedfn = input("What should we call the finished archive? ")
        with zipfile.ZipFile(zippedfn, "w", zipfile.ZIP_DEFLATED) as zipfileobj:
            #create a zip file object
            zipdir(dirpath, zipfileobj) #call to our function
    else:
        print("Run the script again when you have a valid directory to zip")

main()


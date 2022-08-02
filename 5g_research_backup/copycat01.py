#!/usr/bin/env python3
import shutil #lets us access shell utility
import os


#move to the working directory
os.chdir("/home/student/mycode/") 

#copy the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy all directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")


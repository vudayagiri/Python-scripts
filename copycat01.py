#! /usr/bin/env python3

import os
import shutil
import glob
import copyreg


os.chdir("C:\\Users\\v227377\PycharmProjects\Python_training")
#shutil.copy("5G_Research\sdn_network.txt","5G_Research\sdn_network.txt.copy")



for fils in glob.glob('Python_training\sdn*'):
    print(fils)
   #shutil.copy(files,"5G_Research_backup\"")



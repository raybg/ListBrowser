import pandas as pd
import numpy as np
import shutil
from shutil import *
import csv

shutil.copyfile("C:\\Cogencis WorkStation\\TMP\\Specific\\Common\\QUOTELISTS2.TXT", "C:\\Users\\g.bhargavi\\Desktop\\owtest12.csv")

lb = open("C:\\Users\\g.bhargavi\\Desktop\\owtest12.csv", "r+")
lb = lb.read()
lb1 = lb.replace("|",",")

f= open("C:\\Users\\g.bhargavi\\Desktop\\owtest13.txt", "w+")
f.write(lb1)
shutil.copyfile("C:\\Users\\g.bhargavi\\Desktop\\owtest13.txt","C:\\Users\\g.bhargavi\\Desktop\\owtest13.csv")

lb2 = lb1.replace("@",",")
f = open("C:\\Users\\g.bhargavi\\Desktop\\owtest14.txt", "w+")
f.write(lb2)
shutil.copyfile("C:\\Users\\g.bhargavi\\Desktop\\owtest14.txt","C:\\Users\\g.bhargavi\\Desktop\\owtest14.csv")

#f=open("C:\\Users\\g.bhargavi\\Desktop\\owtest14.csv","w+")
#f.write()
#f.to_text("C:\\Users\\g.bhargavi\\Desktop\\owtest15.txt",index=False, sep=",")
 


#lb3 = lb2.replace(";",",")
#f = open("C:\\Users\\g.bhargavi\\Desktop\\owtest15.txt", "w+")
#f.write(lb3)
#e = shutil.copyfile("C:\\Users\\g.bhargavi\\Desktop\\owtest15.txt","C:\\Users\\g.bhargavi\\Desktop\\owtest15.csv")







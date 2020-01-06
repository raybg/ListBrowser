
import shutil
import pandas as pd
from pathlib import Path

shutil.copyfile("C:\\Cogencis WorkStation\\TMP\\Specific\\Common\\QUOTELISTS2.TXT", "C:\\Users\\g.bhargavi\\Desktop\\nowtest12.csv")

lb = open("C:\\Users\\g.bhargavi\\Desktop\\nowtest12.csv", "r+")
lb = lb.read()
x = lb.replace("\n", ",")
x = x.replace("@","")
x = x.replace(";",",")

y = x.split(",",10000)

z = pd.Series(y)
print(z)




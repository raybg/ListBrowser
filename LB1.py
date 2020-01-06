import shutil
import pandas as pd


shutil.copyfile("C:\\Cogencis WorkStation\\TMP\\Specific\\Common\\QUOTELISTS2.TXT", "C:\\Users\\g.bhargavi\\Desktop\\nowtest12.csv")


lb = open("C:\\Users\\BG\\Desktop\\nowtest12.csv", "r+")
lb = lb.read()
x = lb.replace("\n", ",")
y = x.split(",")

z = pd.Series(y)
print(z)

z.to_frame(z,columns=)
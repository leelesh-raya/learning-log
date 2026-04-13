import os, csv

os.chdir(r"C:\Users\Admin\Desktop")
eg = open("eg.csv")
egr=csv.reader(eg)
data=list(egr)
for row in  egr:
    print(egr.line_num)
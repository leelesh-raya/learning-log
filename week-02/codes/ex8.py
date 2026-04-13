# Project: removing the header from cSV files


import os, csv

os.chdir(r"C:\Users\Admin\Desktop")
os.makedirs("newfolder", exist_ok=True)

for csvfile in os.listdir("naics"):
    if not csvfile.endswith(".csv"):
        continue
    readerobj = open(rf"naics\{csvfile}")
    reader = csv.reader(readerobj)
    nohead = []
    for row in reader:
        if reader.line_num == 1:
            continue
        nohead.append(row)
    readerobj.close()
    writerobj = open(os.path.join("newfolder", csvfile), "w", newline="")
    writer = csv.writer(writerobj)
    for row in nohead:
        writer.writerow(row)
    writerobj.close()

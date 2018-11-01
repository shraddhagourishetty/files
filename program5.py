import csv

ifile = open('test.csv', "rb")
reader = csv.reader(ifile)
ofile = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter='', quotechar='"', quoting=csv.QUOTE_ALL)

for row in reader:
    writer.writerow(row)

ifile.close()
ofile.close()
import csv

data1 = []
data2 = []

with open("dataset1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data1.append(row)

with open("dataset2sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data2.append(row)

header1 = data1[0]
planetdata1 = data1[1:]

header2 = data2[0]
planetdata2 = data2[1:]

headers = header1 + header2

planetdataall = []

for index,data in enumerate(planetdata1):
    combinedata = planetdata1[index] + planetdata2[index]
    planetdataall.append(combinedata)

with open("finaldata.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdataall) 
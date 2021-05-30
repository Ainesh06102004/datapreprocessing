import csv 
data2 = []
with open("dataset2.csv", "r") as f:
    csvread = csv.reader(f)
    for row in csvread:
        data2.append(row)

headers = data2[0]
planetdata = data2[1:]

for data in planetdata:
    data[0] = data[0].lower()

planetdata.sort(key=lambda planetdata: planetdata[0])

with open("dataset2sorted.csv", "a+") as z:
    csvwriter = csv.writer(z)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

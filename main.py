import csv

f = open("legislator.csv")
legislator = csv.reader(f)
l = list(legislator)

gender=[]

for row in l:
  gender.append(row[3])

gender = set(gender[1:])
print(gender)
import csv
f = open("in.txt")
environment=[]	# the data is read on request.
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in rowlist:
        rowlist.append(float(value))
    environment.append(rowlist)
print(environment)
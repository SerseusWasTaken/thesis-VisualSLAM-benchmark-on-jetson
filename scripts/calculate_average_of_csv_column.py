import sys
import csv
from statistics import median

#used to quickly calculate stats for a top output file formated in CSV
#first arg is filename, second is the CSV column to use 

file_name = sys.argv[1]
column = sys.argv[2]

with open(file_name) as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []
    try:
        for row in reader:
            rows.append(float(row[column]))
        print("Median: " + str(median(rows)))
        print("Average: " + str(round(sum(rows) / len(rows), 2)))
        print("Maximum: " + str(max(rows)))
    except KeyError:
        print("Invalid key. Available keys: " + str(reader.fieldnames))

    
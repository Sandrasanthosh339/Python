import csv
with open('sample.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    print("No Name ")
    print("__________________")
    for row in data:
        print(row['no'], row['name'])
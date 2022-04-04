import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

#1 write the code to read dataset_2_sorted.csv

   
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

#2 write the code to merge the headers


planet_data = []

#3 complete the code to append the data
for index, data_row in enumerate(planet_data_1):
    #planet_data.append()

#4 complete the code to create the final data
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    #csvwriter.writerow()
    #csvwriter.writerows()

    
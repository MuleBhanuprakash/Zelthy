import requests
import csv

# getting data from API
results = requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog')
r = results.status_code
t = results.text
jsondata = results.json()
print(r)

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for j in jsondata:
    if count == 0:
        # Writing headers of CSV file
        header = j.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(j.values())

data_file.close()

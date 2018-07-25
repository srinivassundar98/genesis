# importing the csv module
import csv
from mcq import score
from begin import name, roll

# field names
fields = ['Roll', 'Name', 'Viva', 'Documentation', 'Execution']

# data rows of csv fil
rows = [[str(roll), str(name),str(score) , '', '']]

# name of csv file
filename = "records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
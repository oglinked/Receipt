""" Writes field's names in CSV file"""

import csv
	
# field names
fields = ['TransactionID',
          'CID',
          'Date',
          'Time',
          'Currensy1',
          'Amount1',
          'Currensy2',
          'Amount2',
          'Rate',
          'Comment',
          'General1',
          'General2'
         ]

# name of csv file
filename = "log.csv"
	
# writing to csv file
with open(filename, 'w', encoding='UTF8', newline='') as f:
	csvwriter = csv.writer(f, dialect='excel') # csv writer object
	csvwriter.writerow(fields) # writing the fields

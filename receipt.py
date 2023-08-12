""" WollPay receipt (Version 02.05) """

import random
import datetime
from datetime import date
import pytz
import csv


#The Greeting and the Input Data Block.
print('Hello Host!\nPlease input the Data of the new Transaction.\n')
input_currency = input('Currensy1: ')
input_summ = input('Amount1: ')
output_currency = input('Currensy2: ')
output_summ = input('Amount2: ')
cid = input('CID: ')
comment = input('Input your Comment please: ')
general1 = input('Please input General1: ')
general2 = input('Input General2: ' )

# The calculating of rate.
input_summ_float = float(input_summ)
output_summ_float = float(output_summ)

if input_summ_float >= output_summ_float: 
	rate = input_summ_float / output_summ_float
else:
	rate = output_summ_float / input_summ_float

rate = "{:.2f}".format(rate)

# The random Transaction ID calculating.
transaction_ID = random.randint(10000000, 99999999)
transaction_ID = str(transaction_ID)

# Current Date & Time getting (for Poland).
current_time = datetime.datetime.now(pytz.timezone('Poland')) \
               .strftime('%I:%M %p')
current_date = date.today()
current_date = current_date.strftime("%m/%d/%Y") # mm/dd/YY


# Output to console.
print('\n----------Welcome to WollPay!----------\n')
print('Transfer:       ',
      input_currency,
      input_summ,
      ' --> ',
      output_currency,
      output_summ)
print('Date:           ', current_date)
print('Time:           ', current_time, ' (GMT+2)')
print('TransactionID:  ', transaction_ID)
print('Rate:           ', rate)
print('\nThank you for being a WollPay customer!')
print('----------------WollPay----------------\n\n')

# The printing in receipt.txt file.
with open('receipt.txt', 'w') as f:
	f.write('\n----------Welcome to WollPay!----------\n')
	f.write('\nTransfer:       '
	        + input_currency 
	        + ' '
	        + input_summ
              + ' --> ' 
	        + output_currency
		    + ' ' 
	        + output_summ)
	f.write('\nDate:           ' + current_date)
	f.write('\nTime:           ' + current_time + ' (GMT+2)')
	f.write('\nTransactionID:  ' + transaction_ID)
	f.write('\nRate:           ' + rate)
	f.write('\n\nThank you for being a WollPay customer!\n')
	f.write('----------------WollPay----------------\n\n')
	 
# The printing in the log.csv file.
row = [transaction_ID,
       cid,
       current_date,
       current_time,
       input_currency,
       input_summ,
       output_currency,
       output_summ,
       rate,
       comment,
       general1,
       general2
      ]
filename = "log.csv"
with open(filename, 'a', encoding='UTF8', newline='') as f:
	csvwriter = csv.writer(f, dialect='excel')
	csvwriter.writerow(row)

input('Click "ENTER" to exit: ')

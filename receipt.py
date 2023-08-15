""" WollPay Receipt (Version 03.01) """

import random
import datetime
from datetime import date
import pytz
import csv
from pathlib import Path


#The Greeting and the Input Data Block.
print('Hello Host!')

# The getting Path to log.csv file.
result = 'n'
result = input('Would you like to input the PATH\n \
to log.csv file destination Folder? (y/n): ')
if result == 'y' or result == 'Y':
    path_to_folder = input('Path to destination folder:  ')
    filename = path_to_folder + '/log.csv'
else:
    filename = 'log.csv'

print('Path to file:  ',filename) # To test only

# The transactions cycle.
i = 'y'
while i == 'y' or i == 'Y':
    print('Please input the Data of the new Transaction.')
    cid = input('CID: ')
    input_currency = input('CurrencyIn: ')
    input_summ = input('AmountIn: ')
    output_currency = input('CurrencyOut: ')
    output_summ = input('AmountOut: ')
    comment = input('Input your Comment please: ')
    cash_in = input('Please input CashRegistrarIn ')
    cash_out = input('Input CashRegistrarOut ')
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
    transaction_ID = random.randint(100000000000, 999999999999)
    transaction_ID = str(transaction_ID)

    # Current Date & Time getting (for Poland).
    current_time = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime('%I:%M %p')
    # current_date = date.today()
    # current_date = current_date.strftime("%m/%d/%Y") # mm/dd/YY

    # Input the current date manualy.
    result = 'n'
    result = input('Would you like to input Date manualy? (y/n): ')
    if result == 'y' or result == 'Y':
        current_date = input('Please input the Date you prefer: ')
    else:
        # current_date = date.today()
        # current_date = current_date.strftime("%m/%d/%Y") # mm/dd/YY
        current_date = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime("%m/%d/%Y")
    time_zone = 'GMT+2'

    #The Receipt printing (the output to console).
    print('\n\n----------Welcome to WollPay!----------\n')
    print('Transfer:       ',
        input_currency,
        input_summ,
        ' --> ',
        output_currency,
        output_summ)
    print('Date:           ', current_date)
    print('Time:           ', current_time, ' ', '(' + time_zone + ')')
    print('TransactionID:  ', transaction_ID)
    print('Rate:           ', rate)
    print('\nThank you for being a WollPay customer!')
    print('----------------WollPay----------------\n\n')

    # The receipt appanding in receipt.txt file.
    with open('receipt.txt', 'a') as f:
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
        f.write('\nTime:           ' + current_time 
                                    + ' ' + '(' + time_zone + ')')
        f.write('\nTransactionID:  ' + transaction_ID)
        f.write('\nRate:           ' + rate)
        f.write('\n\nThank you for being a WollPay customer!\n')
        f.write('----------------WollPay----------------\n\n')
        
    # log.csv file data:

    # field names
    fields = [
            'TransactionID',
            'CID',
            'Date',
            'Time',
            'TZ',
            'CurrencyIn',
            'AmountIn',
            'CurrencyOut',
            'AmountOut',
            'Rate',
            'Comment',
            'CashRegistrarIn',
            'CashRegistrarOut',
            'General1',
            'General2'
            ]
    # Fields values.
    row = [
        transaction_ID,
        cid,
        current_date,
        current_time,
        time_zone,
        input_currency,
        input_summ,
        output_currency,
        output_summ,
        rate,
        comment,
        cash_in,
        cash_out,
        general1,
        general2
        ]

    # Checking the log.csv file existing and writing to log.csv.
    path = Path(filename)
    result = path.is_file()

    if result == True:
        with open(filename, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(filename, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('Would you like to input another Transaction? (y/n): ')

input('Click "ENTER" to exit: ')

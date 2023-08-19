""" WollPay Receipt (Version 03.04 with partly Validation) """

import random
import datetime
from datetime import date
import pytz
import csv
from pathlib import Path
import os

def str_valid_to_upper(str_to_valid):
    """ String validation.
    Capital letters only. No numbers.
    str_to_valid  parametr (Input string to validation).
    """
    if str_to_valid.isalpha():
        pass
    else:
        print('Error: Only letters without spaces \
are allowed in this field!')
        # print(f'Your input was "{str_to_valid}".')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.
    str_to_valid = str_to_valid.upper()
    return str_to_valid  


def isfloat(num):
    """Python Program to Check If a String Is a Number (Float)"""
    try:
        float(num)
        return True
    except ValueError:
        return False
    

def valid_number(number):
    """ Number validation.
    Numbers only. Commas and Dots are allowed as digit separators.
    number - parametr (Input string to validation).
    """
    if number.isdecimal():
        pass
    elif isfloat(number):
        pass
    else:
        print('Error: Only decimal digits (and wone dot) \
are allowed in this field!')
        number = input('Please repeat input: ')
        number = valid_number(number) # Recursion.
    return number    


log_name = 'log.csv' # The file where log will be written.
time_zone = 'GMT+2' # For Poland.



# The transactions loope.
i = 'y'
while i != 'q':
    os.system('cls') # Clearing the Screen.

    #The Greeting & information.
    print('Hello Host!')
    print('Please input the Data of the new Transaction.')
    print('\nFull Path to log.csv file is: \n' + os.path.abspath(log_name))
    input('\nClick "ENTER" to input the Data: ')
    
    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    input_currency = input('Currency IN: ')
    input_currency = str_valid_to_upper(input_currency)
    input_summ = input('Amount IN: ')
    input_summ = valid_number(input_summ)
    output_currency = input('Currency OUT: ')
    output_currency = str_valid_to_upper(output_currency)
    output_summ = input('Amount OUT: ')
    output_summ = valid_number(output_summ)
    comment = input('Comment: ')
    cash_in = input('Cash Registrar IN: ')
    cash_in = valid_number(cash_in)
    cash_out = input('Cash Registrar OUT: ')
    cash_out = valid_number(cash_out)
    new_client_data = input('New data about client: ')
    general1 = input('General1: ')
    general2 = input('General2: ' )
    
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
    # Current Time:
    current_time = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime('%I:%M %p')

    # Input the current date manualy or get from Inet.
    current_date = input('Date: ')
    if len(current_date) < 2:
        current_date = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting date from Inet.
    else:
        current_date = current_date

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
    # field names:
    fields = [
            'TransactionID',
            'Date',
            'Time',
            'TZ',
            'CID',
            'Currency1',
            'Amount1',
            'Currency2',
            'Amount2',
            'Rate',
            'Comment',
            'CashRegistrarIN',
            'CashRegistrarOUT',
            'NewData',
            'General1',
            'General2'
            ]
    # Fields values.
    row = [
        transaction_ID,
        current_date,
        current_time,
        time_zone,
        cid,
        input_currency,
        input_summ,
        output_currency,
        output_summ,
        rate,
        comment,
        cash_in,
        cash_out,
        new_client_data,
        general1,
        general2
        ]

    # Checking the log.csv file existing and writing to log.csv.
    path = Path(log_name)
    result = path.is_file()

    if result == True:
        with open(log_name, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(log_name, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('\nAnother Transaction? (Click "q" to exit) : ')

input('Click "ENTER" to exit: ')

""" WollPay Receipt (Version 03.09 of receipt.py program). """

import random
import datetime
import pytz
import csv
import os
from pathlib import Path
import re


def cyrillic_presence_test(str_to_valid):
    """No cyrillic letters please."""
    result = re.findall("[а-яА-Я]", str_to_valid)
    if not bool(result):
        pass
    else:
        print('Error: No cyrillic letters are allowed in this field!')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid) # Recursion.
    return str_to_valid


def str_valid_to_upper(str_to_valid):
    """ String validation.
    Capital letters only. No numbers.
    str_to_valid  parametr (Input string to validation).
    """
    str_to_valid = cyrillic_presence_test(str_to_valid)
    if str_to_valid.isalpha():
        pass
    else:
        print('Error: Only letters without spaces \
are allowed in this field!')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid)
        str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.
    str_to_valid = str_to_valid.upper()
    return str_to_valid  


def isfloat(num):
    """Python Program to Check If a String Is a Number (Float)"""
    num = cyrillic_presence_test(num)
    try:
        float(num)
        return True
    except ValueError:
        return False
    

def valid_number(number):
    """ Number validation.
    Numbers only. Dots are allowed to float numbers.
    number - parametr (Input string to validation).
    """
    number = cyrillic_presence_test(number)
    number = remove_whitespaces(number)
    if number.isdecimal():
        pass
    elif isfloat(number):
        pass
    else:
        print('Error: Only decimal digits (and one dot) \
are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number)
        number = valid_number(number) # Recursion.
    return number    


def valid_decimal(number):
    """ Number validation.
    Decimal digits are allowed only.
    number - parametr (Input string to validation).
    """
    number = cyrillic_presence_test(number)
    number = remove_whitespaces(number)
    if number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number)
        number = valid_decimal(number) # Recursion.
    return number    


def remove_whitespaces(string):
    """Code to remove whitespaces"""
    return string.replace(" ", "")


def check_letters(string):
    """Checking for absence of letters in given string."""
    string = cyrillic_presence_test(string)
    result = True # Initializing result variable.
    for i in string:
        if i.isalpha(): # if string has letter:
            result = False
    return result


def empty_date(date):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave the field empty y/n?.
    """
    date = cyrillic_presence_test(date)
    if date == '':
        date = force_empty_date(date)
    else:
        date = date_validation(date)
    return date


def force_empty_date(date):
    """Empty (or current) date."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result)
    if result in ['y', 'Y']:
        # date = '' # Empty field.
        date = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime("%m/%d/%Y") # Getting current date.
    else:
        date = date_validation(date)
    return date


def date_validation(date):
    """ Date validation.
    date - parameter (Inputed date to validation).
    """
    date = cyrillic_presence_test(date)
    date = remove_whitespaces(date) # To remove whitespaces.
    # Testing the length of the field.
    if len(date) == 10:
        pass
    else:
        print('Error: In this field should be 10 characters.')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    # Testing the absence of alphabetical letters.
    if check_letters(date):
        pass
    else:
        print('Error: No letters are allowed in this field!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    #Testing the presence of two "/" characters.
    if date[2] == date[5] == '/':
        pass
    else:
        print('Error: Check the presence of "/" characters in right places!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    # Testing "mm" in mm/dd/yyyy
    mm = ['01','02','03','04','05','06','07','08','09','10','11','12']
    month = date[0] + date[1]
    if month in mm:
        pass
    else:
        print('Error: The Month value should be [01,...,12].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    # Testing "dd" in mm/dd/yyyy
    dd = ['01','02','03','04','05','06','07','08','09','10',
          '11','12','13','14','15','16','17','18','19','20',
          '21','22','23','24','25','26','27','28','29','30',
          '31']
    day = date[3] + date[4]
    if day in dd:
        pass
    else:
        print('Error: The Day value should be [01,...,31].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    # Testing "yyyy" in mm/dd/yyyy
    yyyy = ['2022','2023','2024','2025','2026','2027','2028',
            '2029','2030','2031','2032','2033','2034','2035']
    year = date[6] + date[7] + date[8] + date[9]
    if year in yyyy:
        pass
    else:
        print('Error: The Year value should be [2022,...,2035].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date)
        date = empty_date(date)
        if date == '': return date
    return date


def get_date(date):
    """Current date for Poland if argument == ''."""
    date = cyrillic_presence_test(date)
    if date == '': 
        date = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting current date.
    else:
        date = date_validation(date) # Validation.
    return date


def yes_or_no(string_to_valid):
    """Only "y","Y" or "n","N" are allowed."""
    string_to_valid = remove_whitespaces(string_to_valid)
    if string_to_valid in ['y','Y']: 
        string_to_valid = 'Yes'
    elif string_to_valid in ['n','N']:
        string_to_valid = 'No'
    else:
        print('Error: Only "Y" or "N" are allowed in this field!')
        string_to_valid = input('Please repeat input: ')
        string_to_valid = cyrillic_presence_test(string_to_valid)
        string_to_valid = yes_or_no(string_to_valid) # Recursion.
    return string_to_valid


log_path = './log.csv' # The relative path to log.csv file.
time_zone = 'GMT+2' # Time zone for Poland.

# The transactions loope.
i = 'y'
while i not in ['q', 'Q']:
    os.system('cls') # Clearing the Screen.
    
    #The Greeting & information.
    print('Hello Host! \
\nYou run version 03.09 of the program receipt.py.')
    print('Please input the Data of the new Transaction.')
    print('\nFull Path to log.csv file is: \n' 
          + os.path.abspath(log_path) 
          + '\n')
    
    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    cid = cyrillic_presence_test(cid)
    cid = valid_decimal(cid)
    input_currency = input('Currency IN: ')
    input_currency = cyrillic_presence_test(input_currency)
    input_currency = str_valid_to_upper(input_currency)
    input_summ = input('Amount IN: ')
    input_summ = cyrillic_presence_test(input_summ)
    input_summ = valid_number(input_summ)
    output_currency = input('Currency OUT: ')
    output_currency = cyrillic_presence_test(output_currency)
    output_currency = str_valid_to_upper(output_currency)
    output_summ = input('Amount OUT: ')
    output_summ = cyrillic_presence_test(output_summ)
    output_summ = valid_number(output_summ)
    comment = input('Comment: ')
    comment = cyrillic_presence_test(comment)
    cash_in = input('Cash Registrar IN: ')
    cash_in = cyrillic_presence_test(cash_in)
    cash_in = valid_number(cash_in)
    cash_out = input('Cash Registrar OUT: ')
    cash_out = cyrillic_presence_test(cash_out)
    cash_out = valid_number(cash_out)
    new_client_data = input('New data about client: ')
    new_client_data = cyrillic_presence_test(new_client_data)
    covered = input('Covered (Y/N): ')
    covered = cyrillic_presence_test(covered)
    covered = yes_or_no(covered)
    general2 = input('General2: ' )
    general2 = cyrillic_presence_test(general2)
    
    # The calculating of rate.
    input_summ_float = float(input_summ)
    output_summ_float = float(output_summ)
    if input_summ_float >= output_summ_float: 
        rate = input_summ_float / output_summ_float
    else:
        rate = output_summ_float / input_summ_float
    rate = "{:.2f}".format(rate)

    # The Transaction's random ID calculating.
    transaction_ID = random.randint(0, 999999999999)
    transaction_ID = str(transaction_ID).zfill(12)

    # Current Date & Time getting (for Poland).
    current_time = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime('%I:%M %p')

    # Input the current date manualy or get from Inet.
    current_date = input('Date: ')
    current_date = cyrillic_presence_test(current_date)
    current_date = get_date(current_date)

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
            'TID', # TransactionID
            'Date',
            'Time',
            'TZ',  # TimeZone
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
            'Covered',
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
        covered,
        general2
        ]

    # Checking the log.csv file existing and writing to log.csv.
    path = Path(log_path)
    result = path.is_file()

    if result == True:
        with open(log_path, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(log_path, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('\nAnother Transaction? (Press "q" to exit, \
or "Enter" to start all over): ')
    i = cyrillic_presence_test(i)

input('Press "ENTER" to exit: ')

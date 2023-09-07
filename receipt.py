""" WollPay Receipt (Version 03.12 of receipt.py program). """

import random
import datetime
import pytz
import csv
import os
from pathlib import Path
import re

message_cyrillic = 'No cyrillic letters are allowed in this field!'
message_latin = 'Only Latin letters are allowed in this field!'


def cyrillic_presence_test(str_to_valid, message = message_latin):
    """No cyrillic letters please."""
    result = re.findall("[а-яА-Я]", str_to_valid)
    if not bool(result):
        pass
    else:
        print(f'Error: {message}')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid, message)
        # It was Recursion.
    return str_to_valid


def cid_validation(cid):
    """Validation of CID."""
    cid = cyrillic_presence_test(cid, message_cyrillic)
    cid = remove_tabs_and_whitespaces(cid)
    if len(cid) < 1: # Minimum 1 character should be present.
        print('Error: Too few characters are inputted.')
        cid = input('Repeat Input: ')
        cid = cid_validation(cid) # Recursion.
    cid = valid_isalnum(cid) # To test the presence of
    # Latin alphabet and decimal digits only. 
    return cid


def valid_isalnum(str_to_valid):
    """Validation the Latin alphabet and decimal digits
    presence only. It's for field CID only.
    Return latters on the upper case.
    """
    if str_to_valid.isalnum():
        pass
    else:
        print('Error: Only Latin latters and decimal digits \
are allowed in this field.')
        str_to_valid = input('Repeat Input: ')
        str_to_valid = cid_validation(str_to_valid) # Go to CID validation.
    return str_to_valid.upper()


def str_valid_to_upper(str_to_valid):
    """ String validation.
    Capital letters only. No numbers.
    str_to_valid - parameter (Input string to validation).
    """
    str_to_valid = cyrillic_presence_test(str_to_valid)
    str_to_valid = remove_tabs(str_to_valid)
    if str_to_valid.isalpha():
        pass
    else:
        print('Error: Only Latin letters are allowed in this field!')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid)
        str_to_valid = remove_tabs(str_to_valid)
        str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.
    str_to_valid = str_to_valid.upper()
    return str_to_valid  


def isfloat(num):
    """Python Program to Check If a String Is a Number (Float)"""
    num = cyrillic_presence_test(num, message_cyrillic)
    num = remove_tabs_and_whitespaces(num)
    try:
        float(num)
        return True
    except ValueError:
        return False
    

def valid_number(number):
    """ Number validation.
    Numbers only. Dots are allowed to float numbers.
    number - parameter (Input string to validation).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    if number.isdecimal():
        pass
    elif isfloat(number):
        pass
    else:
        print('Error: Only decimal digits (and one dot) \
are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = valid_number(number) # Recursion.
    return number    


def valid_decimal(number):
    """ Number validation.
    Decimal digits are allowed only.
    number - parameter (Input string to validation).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    if number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = valid_decimal(number) # Recursion.
    return number    


def remove_tabs(string):
    """Code to remove tabulation."""
    if '\t' in string:
        print('Warning: Inputted Tabs characters were removed!')
    return string.replace('\t', '')


def remove_whitespaces(string):
    """Code to remove whitespaces"""
    if ' ' in string:
        print('Warning: Inputted whitespaces were removed!')
    return string.replace(" ", "")


def remove_tabs_and_whitespaces(string):
    """Code to remove tabulation and whitespaces."""
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def check_letters(str_to_valid):
    """Checking for absence of letters in given string."""
    str_to_valid = cyrillic_presence_test(str_to_valid)
    str_to_valid = remove_tabs(str_to_valid)
    result = True # Initializing result variable.
    for i in str_to_valid:
        if i.isalpha(): # if string has letter:
            result = False
    return result


def empty_date(date):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave this field empty y/n?.
    """
    date = cyrillic_presence_test(date, message_cyrillic)
    date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
    if date == '':
        date = force_empty_date(date)
    else:
        date = date_validation(date)
    return date


def force_empty_date(date):
    """Empty (or current) date."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs(result)
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
    date = cyrillic_presence_test(date, message_cyrillic)
    date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
    # Testing the length of the field.
    if len(date) == 10:
        pass
    else:
        print('Error: In this field should be 10 characters.')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    # Testing the absence of alphabetical letters.
    if check_letters(date):
        pass
    else:
        print('Error: No letters are allowed in this field!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    #Testing the presence of two "/" characters.
    if date[2] == date[5] == '/':
        pass
    else:
        print('Error: Check the presence of "/" characters in right places!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
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
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
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
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
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
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Removing "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    return date


def get_date(date):
    """Current date for Poland if argument == ''."""
    if date == '':
        date = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting current date.
    else:
        date = date_validation(date) # Validation.
    return date


def yes_or_no(string_to_valid):
    """Only "y","Y" or "n","N" are allowed."""
    # Removing "\t" and " ".
    string_to_valid = remove_tabs_and_whitespaces(string_to_valid) 
    if string_to_valid in ['y','Y']: 
        string_to_valid = 'Y'
    elif string_to_valid in ['n','N']:
        string_to_valid = 'N'
    else:
        print('Error: Only "Y" or "N" are allowed in this field!')
        string_to_valid = input('Please repeat input: ')
        string_to_valid = cyrillic_presence_test(string_to_valid,
                                                message_cyrillic)
        # Removing "\t" and " ".
        string_to_valid = remove_tabs_and_whitespaces(string_to_valid) 
        string_to_valid = yes_or_no(string_to_valid) # Recursion.
    return string_to_valid


def currency_validation(currency):
    """Checks if the currency's input was right."""
    currency = cyrillic_presence_test(currency)
    currency = remove_tabs(currency)
    if len(currency) < 1: # Minimum 1 character should be present.
        print('Error: Too few characters were inputted!')
        currency = input('Repeat Input: ')
        currency = currency_validation(currency) # Recursion.
    currency = str_valid_to_upper(currency)
    return currency


def amount_validation(amount):
    """Amount validation."""
    amount = cyrillic_presence_test(amount, message_cyrillic)
    amount = remove_tabs(amount)
    if len(amount) < 1: # Minimum 1 character should be present.
        print('Error: Too few characters were inputted.')
        amount = input('Repeat Input: ')
        amount = amount_validation(amount) # Recursion.
    amount = valid_number(amount)
    return amount


def remove_cyrillic_and_tabs(string, message=message_latin):
    """Cyrillic + Tabs removing."""
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    return string


def exit_test(i):
    """Exit or continue validation test."""   
    i = cyrillic_presence_test(i, message_cyrillic)
    i = remove_tabs_and_whitespaces(i)
    if i in ['q', '']:
        pass
    else:
        print('Error: only "q" or "Enter" are allowed!')
        i = input('Press "q" to exit, or "Enter" to start all over): ')
        i = exit_test(i) # Recursion.
    return i


log_path = './log.csv' # The relative path to log.csv file.
time_zone = 'GMT+2' # Time zone for Poland.

# The transactions loope.
i = 'y'
while i != 'q':
    os.system('cls') # Clearing the Screen.
    
    #The Greeting & information.
    print('Hello Host! \
\nYou run version 03.12 of the program receipt.py.')
    print('Please input the Data of the new Transaction.')
    print('\nFull Path to log.csv file is: \n' 
          + os.path.abspath(log_path) 
          + '\n')
    
    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    cid = cid_validation(cid)

    input_currency = input('Currency IN: ')
    input_currency = currency_validation(input_currency)
    
    input_summ = input('Amount IN: ')
    input_summ = amount_validation(input_summ)
   
    output_currency = input('Currency OUT: ')
    output_currency = currency_validation(output_currency)

    output_summ = input('Amount OUT: ')
    output_summ = amount_validation(output_summ)
    
    comment = input('Comment: ')
    comment = remove_cyrillic_and_tabs(comment, message_cyrillic)

    cash_in = input('Cash Registrar IN: ')
    cash_in = amount_validation(cash_in)
    
    cash_out = input('Cash Registrar OUT: ')
    cash_out = amount_validation(cash_out)
    
    new_client_data = input('New data about client: ')
    new_client_data = remove_cyrillic_and_tabs(new_client_data,
                                               message_cyrillic)

    covered = input('Covered: ')
    covered = remove_cyrillic_and_tabs(covered)
    covered = yes_or_no(covered)

    general1 = input('General1: ' )
    general1 = remove_cyrillic_and_tabs(general1, message_cyrillic)

    general2 = input('General2: ' )
    general2 = remove_cyrillic_and_tabs(general2, message_cyrillic)
    
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
    print('Time:           ', current_time, '(' + time_zone + ')')
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
        covered,
        general1,
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
    i = exit_test(i)

input('Press "ENTER" to exit: ')

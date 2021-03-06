#!/usr/bin/env python
# IndexingDate_mvp.py

# Prints out a date, given user input of year, month, and day as numbers.

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']

year = input('Year 4 digits: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')

day_number = int(day)
month_number = int(month)
year_number = int(year)

# self check
# details of ordinal day written in english
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
# 1st
# 2nd
# 3rd
# 4th 5th 6th 7th 8th 9th 10th 11th 12th 13th 14th 15th 16th 17th 18th 19th 20th = 17 total
# 21st
# 22nd 
# 23rd
# 24th 25th 26th 27th 28th 29th 30th = 7 total 
# 31st
endings = ['st', 'nd', 'rd'] + 17*['th'] + ['st', 'nd', 'rd'] + 7*['th'] + ['st']

# self check
# len(endings) 
# 31

print("String version", month + '-' + day + '-' + year)
print("Ordinal version", month_number, ' - ', day_number, ' - ', year_number)

# to grab the month 
month_name = months[month_number-1]   # offset month to grab correct index
print("variable month_name: ", month_name, "type: ", type(month_name))
print("variable months: ", month_name, "type: ", type(month_name))
print("variable month_number: ", month_number, "type: ", type(month_number))
print("variable year_number: ", year_number, "type", type(year_number))

ordinal = day + endings[day_number-1]   # offset day_number to grad correct index

print("Corrected Version: ")

print(month_name + ' ' + ordinal, year_number)

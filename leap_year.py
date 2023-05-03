# Write a Python program to check whether a given year is a leap year or not.
# Take a year as input from the user and use the following criteria to determine whether the year is a leap year or not:
# If the year is divisible by 4, it is a leap year.
# If the year is divisible by 100, it is not a leap year.
# If the year is divisible by 400, it is a leap year.
# Display a message indicating whether the year is a leap year or not.
# See reference: https://www.wikihow.com/Calculate-Leap-Years

import calendar

# Testing if a year is a leap year
list_leap_years = [1904,1920,1944,1972,2000,2020,2024]
list_no_leap_years = [1900,2100,2200,2300,2500,2600,2700,2900,3000]
list_mix_years = [1900,1920,1977,2020,2025]

# Function that validates a leap year

def leap_year(year):

    # divided by 100 means century year 
    # century year divided by 400 is leap year

    if (year % 400 == 0) and (year % 100 == 0):
      return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year

    else:
        return False


# function that returns a dictionary with a list of leap or/and no leap years

def leap_year_list(list_years):

    dic_leap = {"LEAP": [], "NO_LEAP": []}

    # looping the list of years to divide into no leap and leap years. 
    for year in list_years:
        if (leap_year(year)):
           dic_leap["LEAP"].append(year)
        else:
            dic_leap["NO_LEAP"].append(year)
    
    # return dictionnary 
    return dic_leap


# Enter a year and convert into integer

year = int(input("Enter a year: "))

# Validate if is a leap year 

if (leap_year(year)):
    print("\nThe given year "+str(year)+" is a leap year")
else:
    print("\nThe given year "+str(year)+" is NOT a leap year !!")


# Testing - validate list of years

# Leap years
print("\nList of LEAP YEARS: "+str(leap_year_list(list_leap_years)['LEAP']))

# No leap years
print("\nList of NO LEAP YEARS: "+str(leap_year_list(list_no_leap_years)['NO_LEAP']))

# Mixed years
print("\nLIST: "+str(leap_year_list(list_mix_years)))


# using calendar library to validate a leap year

if (calendar.isleap(year)):
    print("\nCALENDAR: The given year "+str(year)+" is a leap year\n")
else:
    print("\nCALENDAR: The given year "+str(year)+" is NOT a leap year\n")

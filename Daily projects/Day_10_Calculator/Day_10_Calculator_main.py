"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 10 - Calculator                                                                                   *
*    Subject: Function with output (return keyword)                                                         *
*    Date: 2022-03-13                                                                                       *
*************************************************************************************************************
"""
# Exercise 10.1 - Days in Month
'''Instructions In the starting code, you'll find the solution from the Leap Year challenge. First, convert this 
function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap 
year and return False if it is not a leap year. 

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28 The List month_days contains the number of days in a month from January to December for a non-leap year. A leap 
year has 29 days in February. '''


# Solution code

def is_leap(year_):
    """Returns true if a year is a leap year else returns false"""
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_):
    """This function return the number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month_ in month_days:
        positions = month_days.index(month_ - 1)
        if is_leap(year_) and month_ == 2:
            return 29
        # else:
        return month_days[positions]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year)
print(days)

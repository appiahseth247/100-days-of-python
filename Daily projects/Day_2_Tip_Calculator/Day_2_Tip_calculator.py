"""
*****************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                   *
*    Author: Seth Appiah                                        *
*    Day: 2 - Tip Calculator                                    *
*    Subject: Data types, f-string                              *
*    Date: 2022-02-10                                           *
*****************************************************************
"""



#Day 2.3 Your life in weeks
#This code calculates the number of years, months and days left if you are to live for  90 years
Life_span_in_years = 90
Life_span_in_months = 90*12
Life_span_in_days = 90*365
Life_span_in_weeks = 90*52

age = input("How old are you?\n")
current_age = int(age)

yeas_left = Life_span_in_years - current_age
months_left = Life_span_in_months  - current_age*12
weeks_left= Life_span_in_weeks - current_age*52
days_left = Life_span_in_days - current_age*365

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left')


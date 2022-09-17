"""
*************************************************************************************************************
*    Course: 100 Days of Code - Dr. Angela Yu                                                               *
*    Author: Seth Appiah                                                                                    *
*    Day: 24 -  Analyzing squirrel data                                                                     *
*    Subject:  Intro to CSV and Pandas                                                                      *
*    Date: 2022-05-06                                                                                       *
*************************************************************************************************************
"""

# Day 25 lesson - Data Analysis
import csv
import pandas  # best for reading csv data


# with open("weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()  # the content
#     print(data)
#
#
# with open("weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)  # for reading csv files
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":  # So that the column title "temp" is not printed as well
#             temperature.append(int(row[1]))
#     print(temperature)
#
# data = pandas.read_csv("weather_data.csv")  # Don't to need to open it separately.
# print(data)
# temperature = data["temp"]  # To get the column headed as "temp"
# print(type(data))  # This is of type "DataFrame" which is the equivalent of the whole table in the csv
# print(type(temperature))  # This is of type "Series" which is the equivalent of a single column of a table in the csv
# data_dict = data.to_dict()  # convert to a dictionary
# print(data_dict)
#
# temp_list = data["temp"].to_list()  # create the list
# print(temp_list)
#
# avg_temp = round(sum(temp_list) / len(temp_list))
# print(avg_temp)
#
# print(data["temp"].mean())
# print(f"the max value is {data['temp']}.max()")
#
# TODO:  Get data in column
# print(data["condition"])  # Treated like a dict
# print(data.condition)  # Treated like an object
#
# TODO: Get data in row
# print(data[data.day == "Monday"])  # Get the weather condition of MONDAY
# print(data[data.temp == data.temp.max()])  # Which is equal to the max temp
#
# monday = data[data.day == "Monday"]
# print(32 + monday.temp * 9 / 5)
#
# TODO: How to create a dataframe from scratch
# data_dict = {
#     "students": ["A", "Kofi", "Ama"],
#     "score": [12, 34, 45],
# }
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("student_score_new_data.csv")
# print(data2)

# TODO: Getting the squirrel count from the 2018 data
# data_list = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_count = data_list["Primary Fur Color"].value_counts()
# print(color_count)
#
# squirrel_count = pandas.DataFrame(color_count)
# squirrel_count.to_csv("squirrel_count.csv")
# print(squirrel_count)

# Second method
data_list = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data_list[data_list["Primary Fur Color"] == "Gray"])
red_color_count = len(data_list[data_list["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data_list[data_list["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [gray_color_count, red_color_count, black_color_count],
}
squirrel_count_df = pandas.DataFrame(data_dict)
squirrel_count_df.to_csv("squirrel_counts.csv")
print(gray_color_count)

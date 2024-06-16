# with open("./weather_data.csv", "r") as weather_file:
#     data = weather_file.readlines()
#     print(data)

"""
import csv

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
"""

# import pandas
#
# data = pandas.read_csv("weather_data.csv")

# Dataframe
# data_dict = data.to_dict()
# print(data_dict)

# Series
# temperatures = data["temp"].to_list()
# print(temperatures)

# avg = sum(temperatures) / len(temperatures)
# print(avg)

# print(data["temp"].mean())
# print(data["temp"].mode())
# print(data["temp"].median())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_celc = monday.temp[0]
# monday_temp_fahr = monday_temp_celc * 9/5 + 32
# print(monday_temp_fahr)

# Create a Dataframes from scratch

# student_report = {
#     "students": ["Handika", "Ridho", "Rosidah Lia", "Syamsudin"],
#     "scores": [90, 88, 85, 88],
# }
#
# data_student = pandas.DataFrame(student_report)
# print(data_student)
#
# # Convert to csv
# data_student.to_csv("student_report.csv")

# Challenge day 25

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")

""" List Comprehension
syntax:
new_list = [new_item for item in list]
"""

# # list
# numbers: list[int] = [1, 2, 3, 4, 5]
# new_numbers: list[int] = [n * 2 for n in numbers]
# print(new_numbers)
# # string
# name: str = "Handika"
# letters_list: list[str] = [letter for letter in name]
# print(letters_list)
# # range
# numbers2: list[int] = [n * 2 for n in range(1, 5)]
# print(numbers2)

""" Conditional list comprehension
syntax:
new_list = [new_item for item in list if test]
"""

# names: list[str] = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names: list[str] = [name for name in names if len(name) < 5]
# print(short_names)

# long_names: list[str] = [name.upper() for name in names if len(name) > 5]
# print(long_names)

""" Dictionary Comprehension
syntax:
new_dict = {new_key: new_value for item in list}

# Berdasarkan nilai dalam kamus yang sudah ada
new_dict = {new_key: new_value for (key, value) in dict.items()}

# Conditional Dictionary Comprehension
new_dict = {new_key: new_value for (key, value) in dict.items() if test}
"""

# import random
# student_scores = {name: random.randint(1, 100) for name in names}
# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# loop Dataframe
students_data = {
    "student": ["Handika", "Ridho", "Syamsudin", "Rosidahlia"],
    "score": [89, 88, 87, 86]
}

# loop dictionary
# for (key, value) in students_data.items():
#     print(key, value)

import pandas
students_data_frame = pandas.DataFrame(students_data)

# loop through data frame
# for (key, value) in students_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, value) in students_data_frame.iterrows():
    # print(index)
    print(value.student)
    print(value.score)
"""
try:
    file = open('a_file.txt')
    people = {"name": "Handika"}
    print(people["name"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Handika orang paling ganteng didunia-nya sendiri")
except KeyError as err_message:
    print(f"The key {err_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # raise TypeError("This error message made by me:).")
    file.close()
    print("File was closed.")
"""

height = float(input("Height in M: "))
weight = int(input("Weight in Kg: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

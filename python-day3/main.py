# Control Flow with if / else and Conditional Operators

"""
1. == (sama dengan): x == y (True jika x sama dengan y)

2. != (tidak sama dengan): x != y (True jika x tidak sama dengan y)

3. < (kurang dari): x < y (True jika x kurang dari y)

4. > (lebih besar dari): x > y (True jika x lebih besar dari y)

5. <= (kurang dari atau sama dengan): x <= y (True jika x kurang dari atau sama dengan y)

6. >= (lebih besar dari atau sama dengan): x >= y (True jika x lebih besar dari atau sama dengan y)
"""

"""
1. AND (and):
Mengembalikan True jika kedua operandnya adalah True.

2. OR (or):
Mengembalikan True jika salah satu operandnya adalah True.

3.NOT (not):
Mengembalikan kebalikan dari nilai operandnya.
"""

"""
Falsy value pada python:
1. Angka 0: Angka 0 dianggap sebagai False.
2. String kosong (''): String tanpa karakter dianggap sebagai False.
3. List, Tuple, Set, dan Dictionary kosong: Struktur data tanpa elemen dianggap sebagai False.
"""

print("Welcome to the rollercoaster!")
height = int( input("What is Your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster :)")
  age = int( input("What is Your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be oke, Have a free ride on us!")
  else:
    bill = 8
    print("Adult tickets are $12.")
  
  wants_photo = input("Do You want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, You have to grow taller before You can go ride. :(")


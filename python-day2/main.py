# Data Types

# 1. String => kumpulan karakter yg diawali dan diakhiri dgn petik satu('') atau petik dua ("");
"Handika Ganteng"
'123'
# Subscript
print("Hello"[4])

# Integer => Bilangan bulat yang tidak memiliki bagian desimal dan bisa positif, negatif, atau nol.
print(26 + 9)

""" Jika kita memiliki angka yang banyak kita bisa menambahkan underscore, manfaatnya hanya agar kita manusia bisa memvisualisasikannya dgn lebih mudah. """
print(10_000_000) # output: 10000000

# Float => Merepresentasikan bilangan riil yang dapat memiliki bagian desimal atau pecahan.
PI = 3.14159
print(PI)

# Boolean => Mengatur alur logika pemrograman.
True
False

##########################

# Type Checking
# function type() menge-Check type data
# print(type(23))

# Type Conversion
# num_char = len( input("What is Your name? "))

"""
function str() meng-Conversion type data menjadi String.
function int() meng-Conversion type data menjadi Integer number.
function float() meng-Conversion type data menjadi Floating number.
"""

# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " character.")

# Mathematical Operations in Python
"""
Penjumlahan: a + b
Pengurangan: a - b
Perkalian: a * b
Pembagian: a / b; hasil pembagian akan bertipe Float
Modulus (Sisa Pembagian): a % b
Pangkat: a ** b
"""

"""
Operator precedence (urutan prioritas operator) dalam Python menentukan urutan evaluasi ekspresi matematika. Dalam ekspresi yang melibatkan beberapa operator, operator dengan precedence yang lebih tinggi dievaluasi lebih dahulu. Berikut adalah beberapa operator dengan urutan precedence dari yang tertinggi hingga terendah:

PEMDAS(LR = Left to Right)
Parentheses
Exponent
Multipication, Division
Addition, Subtaction

1. Kurung ( ) Ekspresi dalam kurung dievaluasi terlebih dahulu.
2. Pangkat ** Operator pangkat.
3. Positif dan negatif unary +x, -x Positif dan negatif unary.
4. Perkalian, Pembagian, Modulus *, /, % Operasi perkalian, pembagian, dan modulus.
5. Penjumlahan dan Pengurangan +, - Operasi penjumlahan dan pengurangan.
6. Perbandingan <, >, <=, >=, ==, != Operasi perbandingan.
7. Logika boolean not, and, or Operasi logika boolean.
"""
print(3 * (3 + 3) / 3 - 3)

# Membulatkan nilai
print(8 / 3) # Output: 2.66666666666
print(round(8 / 3)) # Output: 3
print(round(5 / 2)) # Output: 2
print(round(2.666666666, 2)) # Output: 2.67

"""
Floor division dalam Python menggunakan operator "//" dan menghasilkan bilangan bulat terbesar yang kurang dari atau sama dengan hasil pembagian dua bilangan. Contoh: 10 // 3 menghasilkan 3. Floor division berguna untuk mendapatkan hasil pembagian dalam bentuk bilangan bulat tanpa memperhatikan sisa pembagian.
"""
print(8 // 3) # Output: 2

"""
Assignment operator shorthand pada Python adalah cara singkat untuk melakukan operasi pengisian nilai pada suatu variabel dengan menggunakan operasi matematika. Contoh-contoh termasuk += untuk penambahan, -= untuk pengurangan, *= untuk perkalian, /= untuk pembagian, %= untuk modulus, dan //= untuk floor division. Ini membantu membuat kode lebih ringkas.
"""
x = 5
x += 3  # Sama dengan x = x + 3

y = 10
y -= 2  # Sama dengan y = y - 2

z = 7
z *= 4  # Sama dengan z = z * 4

w = 12
w /= 3  # Sama dengan w = w / 3

a = 20
a %= 6  # Sama dengan a = a % 6

b = 15
b //= 4  # Sama dengan b = b // 4

"""
F-string (formatted string literal) pada Python adalah cara yang nyaman dan ekspresif untuk memformat string dengan menyisipkan nilai variabel langsung ke dalam string menggunakan kurung kurawal {}. F-string diperkenalkan pada Python 3.6, memberikan sintaks yang jelas dan mudah dibaca serta memungkinkan penggunaan ekspresi Python di dalamnya untuk evaluasi nilai. F-string menyederhanakan proses formatting string dibandingkan dengan metode lama seperti % formatting atau str.format().
"""
name = "Handika"
age = 20

# Menggunakan f-string untuk memasukkan nilai variabel ke dalam string
message = f"My name is {name} and I am {age} years old."

print(message)


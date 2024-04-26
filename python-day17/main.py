"""
snake_case
camelCase
PascalCase => penamaan untuk class
"""

"""
attributes => variable dalam object
method => function dalam object
"""

"""
Constructor functions dalam Python adalah metode khusus yang digunakan untuk menginisialisasi objek saat objek tersebut dibuat. Dalam Python, constructor diimplementasikan menggunakan metode khusus yang disebut __init__(). constructor functions akan dipanggil otomatis saat object dibuat


Dalam Python, self adalah parameter yang digunakan dalam definisi metode di dalam sebuah kelas. Parameter ini merujuk pada objek instans dari kelas tersebut. Ketika Anda membuat metode di dalam sebuah kelas, Anda perlu menyertakan parameter self sebagai argumen pertama dalam definisi metode tersebut. Ini memungkinkan metode tersebut untuk mengakses atribut dan metode dari objek yang dipanggilnya.
"""

# keyword pass untuk
class User:
    # constructor function
    def __init__(self, id, username):
        self.id = id
        self.username = username
        # default value of attribute
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(26, "han_dicca")
user_2 = User(58, "rxdxo")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


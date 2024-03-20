######### Scope #########

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#     # output: enemies inside function: 2
    
# increase_enemies()
# print(f"enemies outside function: {enemies}")
# output: enemies outside function: 1

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion()
# print(potion_strength) Error karena potion_strength tidak didefinisikan di Global Scope

# Global Scope

player_health = 10

def game():
    def potion():
        potion_strength = 2
        print(player_health)
        
    potion()
    
game()
print(player_health)

"""
Python tidak memiliki block scope seperti beberapa bahasa pemrograman lainnya seperti C++ atau Java.
Variabel yang dideklarasikan di dalam suatu blok kode (seperti blok if, blok for, atau blok while) 
masih dapat diakses di luar blok tersebut.
"""

if True:
    x = 10

print(x)  # Output: 10

"""
Namun, ada pengecualian dalam Python, yaitu dengan fungsi. Variabel yang dideklarasikan di dalam 
suatu fungsi hanya dapat diakses di dalam fungsi tersebut, sehingga fungsi memiliki "scope" yang 
terbatas pada fungsi itu sendiri.
"""

def my_function():
    y = 20

my_function()
# print(y)  # Akan menimbulkan NameError: name 'y' is not defined

# Modifying Global Scope
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

global_var = 10

def ubah_var_global(nilai_baru):
    global global_var
    global_var = nilai_baru

print("Nilai variabel global sebelum diubah:", global_var)
ubah_var_global(20)
print("Nilai variabel global setelah diubah:", global_var)

"""
Praktik mengubah variabel global menggunakan kata kunci `global` dalam fungsi di Python dapat menjadi
sumber kebingungan dan kompleksitas dalam kode, terutama saat aplikasi Anda tumbuh lebih besar
"""

""" Global Constant
    => Varibale yang anda tentukan dan anda tidak pernah berencana untuk mengubahnya lagi, itu hanya
    sesuatu seperti misalnya niali PI(π) = 3.141592653589793
    
    Jika Anda ingin membuat variabel global yang bersifat konstan, Anda bisa mengikuti beberapa praktik umum seperti:

    1. Gunakan Huruf Kapital: Konvensi umum dalam pemrograman adalah menggunakan huruf kapital untuk nama variabel yang dianggap konstan. Misalnya, PI daripada pi.

    2. Jangan Ubah Nilainya: Setelah Anda menetapkan nilai awal untuk variabel konstan, pastikan untuk tidak mengubahnya di tempat lain dalam kode. Ini membantu mencegah perubahan tak disengaja.

    3. Dokumentasikan Dengan Jelas: Pastikan untuk mendokumentasikan bahwa variabel tersebut dimaksudkan sebagai konstanta dan bahwa nilainya seharusnya tidak diubah.
"""
PI = 3.141592653589793
GRAVITY = 9.81

def hitung_luas_lingkaran(jari_jari):
    return PI * jari_jari ** 2

def hitung_kecepatan_jatuh(waktu):
    return GRAVITY * waktu

# Contoh penggunaan konstanta
print("Luas lingkaran dengan jari-jari 5 adalah:", hitung_luas_lingkaran(5))
print("Kecepatan jatuh setelah 2 detik adalah:", hitung_kecepatan_jatuh(2))


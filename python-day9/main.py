# {key: value}


programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    1: "satu",
}

"""
    key dalam dictionary bisa berupa objek apa pun yang bersifat hashable (dapat di-hash). Objek yang
    hashable adalah objek yang memiliki nilai hash yang tetap selama hidupnya. Ini berarti bahwa kunci
    dalam dictionary harus bersifat tidak berubah (immutable). Beberapa contoh tipe data yang dapat 
    digunakan sebagai kunci dalam dictionary termasuk: String, Angka(int/float/bilangan kompleks),
    Tuple(jika semua elemennya juga bersifat hashable), boolean, dan tipe data bersifat hashable.
    
    Namun, tipe data yang bersifat mutable seperti list atau dictionary tidak bisa digunakan sebagai kunci karena mereka dapat berubah nilainya setelah dimasukkan ke dalam dictionary, yang akan mempengaruhi hash dan mengganggu struktur internal dictionary.
"""


# Mengakses nilai berdasarkan key
print(programming_dictionary["Bug"])
print(programming_dictionary[1])

# Menambahkan element pada dictionary
programming_dictionary["loop"] = "The action of doing something over and over again."

# Mengubah value yang terikat pada key
programming_dictionary["Bug"] = "The cat in you computer."

# Menghapus pasangan kunci-nilai dari dictionary
del programming_dictionary[1]
print(programming_dictionary)

# Menghapus semua element pada dictionary
# programming_dictionary.clear()
# programming_dictionary = {}
# print(programming_dictionary)

# loop dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])
    
# Nesting
# Nesting a List in a Dictionary
# travel_log = {
#     "Indonesia": ["Lampung", "Bangka Belitung", "Jawa Barat"],
#     "Japan": ["Tokyo", "Osaka", "Shibuya"]
# }

# Nesting a Dictionary in a Dictionary
# travel_log = {
#     "Indonesia": {"city_visited": ["Lampung", "Bangka Belitung", "Jawa Barat"], "total_visited": 3},
#     "France": {"city_visited": ["Paris", "Lille", "Dijon"]},
#     "Germany": {"city_visited": ["Berlin", "Hamburg", "Stuttgart"]},
# }

# print(travel_log["Indonesia"]["city_visited"])

# Nesting a Dictionary in a list
travel_log = [
    {
        "country": "Indonesia",
        "city_visited": ["Lampung", "Bangka Belitung", "Jawa Barat"],
        "total_visited": 3,
    },
    {
        "country": "France",
        "city_visited": ["Paris", "Lille", "Dijon"],
        "total_visited": 0,
    },
    {
        "country": "Germany",
        "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 0,
    }
]
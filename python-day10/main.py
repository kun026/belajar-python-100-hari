# Functions with Output

def format_name(f_name, l_name):
    """
    Convert the given first name and last name to title case.

    Parameters:
    f_name (str): The first name to be converted to title case.
    l_name (str): The last name to be converted to title case.

    Returns:
    str: A string containing the title case version of the first name and last name.
    """
    title_case = f"{f_name} {l_name}".title()
    return title_case
    # print("ini tidak akan pernah dijalankan karena return menandakan berakhirnya suatu function")

formated_string = format_name("hANDika", "syAM")
print(formated_string)

print(format_name("riDHO", "sYAM"))

"""
Docstrings adalah string literal yang muncul tepat setelah definisi header suatu fungsi, metode, kelas,
atau modul dalam bahasa pemrograman Python. Mereka digunakan untuk mendokumentasikan kode tersebut 
dengan cara yang terstruktur dan terorganisir. Docstrings sangat berguna untuk memberikan informasi 
tentang fungsi atau modul kepada pengguna lain atau kepada diri sendiri di masa mendatang.
"""
import random
from art import logo

# Menentukan jumlah percobaan untuk setiap tingkat kesulitan
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

# Menampilkan logo permainan
print(logo)
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")

# Fungsi untuk menentukan tingkat kesulitan permainan
def set_difficulty():
    """
    Prompt the user to choose the game difficulty level.
    
    Returns:
        int: The number of attempts according to the selected difficulty level.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS
    
# Mengambil jumlah percobaan sesuai dengan tingkat kesulitan yang dipilih
attempts = set_difficulty()
# Menghasilkan angka acak antara 1 dan 100 sebagai jawaban
answer = random.randint(1, 100)

# Inisialisasi status permainan
game_end = False

# Memulai loop permainan
while not game_end:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = input("Make a guess: ")
    
    # Memastikan input pengguna adalah angka
    if not user_guess.isdigit():
        print("Please enter a valid number.")
        continue
        
    user_guess = int(user_guess)
    
    # Mengecek apakah percobaan pengguna sudah habis
    if attempts == 1:
        print("You've run out of guesses, You Lose.")
        print(f"The correct answer was {answer}.")
        game_end = True
    else:
        # Membandingkan tebakan pengguna dengan jawaban
        if user_guess > answer:
            print("Too high.\nGuess again.")
        elif user_guess < answer:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {answer}")
            game_end = True
            
    # Mengurangi jumlah percobaan yang tersisa setiap kali pengguna menebak
    attempts -= 1

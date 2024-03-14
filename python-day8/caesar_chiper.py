import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    result = []
    if cipher_direction == "decode":
        # untuk menghasilkan minus pada shift_amount
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            result.append(char)
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            result.append(alphabet[new_position])
    
    print(f"The {cipher_direction}d text is {''.join(result)}")
    
print(art.logo)

continue_again = True
while continue_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    ask_continue = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if ask_continue == 'no':
        continue_again = False
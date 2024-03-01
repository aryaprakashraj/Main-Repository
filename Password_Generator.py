import random
import string

def pas_gen(min_lenght, numbers = True , special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght :
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif letters in special:
            has_special = True 
        
        meets_criteria = True

        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special


    return pwd

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers (y/n): ").lower() == 'y'
has_special = input("Do you wnt to have special characters (y/n): ").lower() =='y'
password = pas_gen(min_lenght , has_number, has_special)
print(password)
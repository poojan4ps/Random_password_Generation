import random
import string

def gen_pass(minlength, numbers=True, special_characters= True ):
    letters= string.ascii_letters
    digits= string.digits
    special= string.punctuation

    characters = letters

    if numbers:
        characters+= digits
    if special_characters:
        characters+=special
    
    pwd=''
    meets_criteria= False
    has_number =False
    has_special = False
    
    while not meets_criteria or len(pwd) < minlength:

        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number= True
        elif new_char in special:
            has_special= True

        meets_criteria= True
        if numbers:
            meets_criteria = has_number
        
        if special_characters:
            meets_criteria= meets_criteria and has_special
    
    return pwd


minlength= int(input('Enter the minimum length:'))
has_number = input(' do you want number(y/n)').lower()== 'y'
has_special = input(' do you want to have special charcaters (y/n)').lower()=='y'
pwd= gen_pass(minlength, has_number, has_special)
print('Generated Password is: ',pwd)
        



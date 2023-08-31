import string
import random

length = int(input("length of password must me 8 Character: "))

print('''Choose different character which makes password strong: 
      1.Digits
      2.Letters
      3.special characters
      4.capital letters
      5.password iss matched to criteria ''')

CharacterList = ""

while(True):
    choice = int(input("pick a digits "))
    if(choice == 1):

        CharacterList +=string.ascii_letters
    elif(choice == 2):

        CharacterList +=string.digits
    elif(choice == 3):

        CharacterList +=string.punctuation
    elif(choice == 4):

        CharacterList +=string.ascii_uppercase
    elif(choice == 5):
        break
    else:
        print("please check the password!")

password = []

for i in range(length):

    randomchar = random.choice(CharacterList)
    password.append(randomchar)

print("your random password is " + "".join(password))

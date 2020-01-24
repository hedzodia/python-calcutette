import os
while True:
    userInput = input("choisir le mode de la calculatrice \n addition soustraction multiplication division quit \n  ")
    os.system('cls')
    if userInput == "quit":
        break
    elif userInput == "addition": 
         print("addition")
         a = input("nombre 1  ")         
         b = input("nombre 2  ")
         print(str(int(a)+int(b))+"\n")
    elif userInput == "soustraction":
         print("soustraction")
         a = input("nombre 1  ")         
         b = input("nombre 2  ")
         print(str(int(a)-int(b))+"\n")
    elif userInput == "multiplication":
         print("multiplication")
         a = input("nombre 1  ")         
         b = input("nombre 2  ")
         print(str(int(a)*int(b))+"\n")
    elif userInput == "division":
         print("division")
         a = input("nombre 1  ")         
         b = input("nombre 2  ")
         print(str(int(a)/int(b))+"\n")
    else : 
        print("mauvaise fonction  \n")
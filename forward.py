print("hey there ")
height = int(input("Enter your height in cm "))
bill = 0

if height >= 120:
    print("welcome to the park!")
    age = int(input("how old are you "))
    if age <= 12:
        print("kids your price is 5$ ")
        bill = 5
   
    elif age <= 18:
        print("teen's your price is 7$ ")
        bill = 7
    
    elif age >= 45 and age <= 55: 
        print("you can ride for free! ")
        bill = 0
    
    else:
        print("adults your price is 15$ ")
        bill = 15


    photo = input("do you want to take a photo? ")
    if photo == "y":
     bill += 3
    print(f"total bill = ${bill}")


else: 
    print("sorry you need to grow taller ")
print("welcome to the leap year checher! ")
number = int(input("Enter a year: "))

if number % 4 == 0 and number %100 == 0 and number %400 == 0:
    print(f"{number}, is leap year")
else:
    print(f"{number}, is not leap year")

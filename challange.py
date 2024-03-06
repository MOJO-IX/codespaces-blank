name1 = input("Enter First Name ")
name2 = input("Enter last Name ")

th = name1 + name2
th = th.count('l') + th.count('o') + th.count('v') + th.count('e')


if th >6:
    print("you have a %90 !")
elif th >= 5 or th > 3:
    print("you have a 70% ! ")
else:
    print("bruh this i bullshit and you know it ")


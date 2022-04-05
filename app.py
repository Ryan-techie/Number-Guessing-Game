import random
num_rand = random.randint(100,999)

tries = 0
while tries < 20:
    var = int(input(">"))
    if var == num_rand:
        print("You won!")
        quit()
    elif var > num_rand:
        print("smaller")
    elif var < num_rand:
        print("greater")
    tries+=1
import random
random_number = random.randint(1,10)
print (random_number)

while True:
    user = int(input("Enter a number: "))
    if user > random_number:
        print ("Your number is bigger then mine")
    elif user < random_number:
        print ("Your number is smaller then mine ")
    else:
        print ("This is the correct number")
        break


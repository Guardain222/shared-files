numbers_list = []

intinal = int(input("Input the ammount of numbers you would like to insert"))

for i in range (intinal):
    numbers = int(input("Please insert the numebrs you have chosen"))
    numbers_list.append(numbers)
print ("No more numbers")
avrage = sum(numbers_list) / intinal
print (avrage)


    



#name = input("Enter your name: ")

#while name == "":
    #print("You dod not enter yout name")
#else:
    #print(f"Hello {name}")   


#age = int(input("Enter your age: "))

#while age < 0:
    #print("Age can not be negative")
    #age = int(input("Enter your age again: "))


#print(f"You are {age} old")

#food = input("Enter a food you like (q to quit): ")

#while not food == "q":
    #print(f"You like {food}")
    #food = input("Enter another food you like (q to quit): ")


#print("bye")    


num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10 please: "))

print(f"Your number is {num}")    
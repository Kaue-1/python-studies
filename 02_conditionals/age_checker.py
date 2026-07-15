age = int(input("What is your age?: "))

if age >100:
    print("You're too old to sign up!")
elif age >=18:
    print("You're now signed up! ")
elif age <0:
    print("You're not even born yet!")

else: 
    print("You must be 18+ to sign up!")

response = input("Woudl you like food? (Y/N): ")
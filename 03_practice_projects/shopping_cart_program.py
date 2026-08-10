#Exercise 2: Shopping Cart Program 

item = (input("What is the item? "))
price = (float(input("What is the price? ")))
quantity = (float(input("How many would you like? ")))

total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}")

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter an noun: (person/place/thing)")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter an verb with an end 'ing': (action) ")
adjective3 = input("Enter an adjective (description): ")


print(f"Today I Went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")
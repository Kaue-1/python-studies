weight = float(input("Enter your weight: "))
unit = input("KG or Pounds?: ")

if unit == "KG":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit} ")    
elif unit == "Pounds":
      weight = weight / 2.205
      unit = "KGs."
      print(f"Your weight is: {round(weight, 1)} {unit} ")    
else: 
     print(f"{unit} was not valid")      
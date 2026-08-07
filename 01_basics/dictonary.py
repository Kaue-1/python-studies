capitals = {"USA": "Washington D.C",
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("Japan"))

#f capitals.get("USA"):
#    print("That capital exists")
#else:
#    print("That capital does not exist")    

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

#print(keys)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
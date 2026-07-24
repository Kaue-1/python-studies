player_health = 100
player_max_health = 250
health_potions = 3
potion_healing = 60
enemy_health = 80
player_damage = 20 
enemy_damage = 15 

print("An enemy has been encountered!!")
print("-------------------------")

while player_health >0 and enemy_health >0:
    print(f"Player Health: {player_health}/{player_max_health} ")
    print(f"Health Potions: {health_potions}")
    print(f"Enemy Health: {enemy_health} ")

    print("-------------------------")

    command = ""
    damage_received = enemy_damage
    while command != "1" and command != "2" and command != "3" and command != "4":
        print("Choose an action:")    
        print("1 - Attack")    
        print("2 - Flee")
        print("3 - Defend")
        print("4 - Heal")    
        command = input("")
    
        if command != "1" and command != "2" and command != "3" and command != "4":
            print("Invalid option!")

    if command == "1":
        enemy_health = enemy_health - player_damage
        print(f"You've dealt {player_damage} damage points!")

        if enemy_health <= 0:
            print("You win!")    
            exit()
    elif command == "2":
        print("You've fled the fight.")
        exit()
    elif command == "3":
        damage_received = damage_received /2
        print("You will defend the next enemy attack!")            
    
    elif command == "4":
        if health_potions > 0:
            if player_health == player_max_health:
                print("Your health is already full!")
            else:   
                current_health = player_health
                if current_health + potion_healing > player_max_health:

                    player_health = player_max_health               
                else:
                    player_health = current_health + potion_healing
                restored_health = player_health - current_health
                print(f"You restored {restored_health} health points!")    
                health_potions = health_potions -1 
        else: 
            print("There are not potions available")
        
    print("------------------------------")

    print("Enemy attacks!")
    player_health = player_health - damage_received
    print(f"You've received {damage_received} damage points! ")

    if player_health <= 0:
        print("You've been defeated!")
        exit()
    
    print("------------------------------")





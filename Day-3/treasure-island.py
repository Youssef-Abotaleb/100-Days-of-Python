print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

if input("Left or right ?  ") == "Left":
    if input("Swim or Wait ?  ") == "Wait":
        Choice = input("Which door ? Red, Blue or Yellow ?  ")
        if Choice == "Red":
            print("You were Burnt by fire. GAME OVER")
        elif Choice == "Blue" :
            print("You were Eaten by beasts. GAME OVER")
        elif Choice == "Yellow" :
            print("You Win !")
        else : print("GAME OVER")
    else :
        print("You were attacked by trout. GAME OVER")
else :
    print("You fell into a hole. GAME OVER.")

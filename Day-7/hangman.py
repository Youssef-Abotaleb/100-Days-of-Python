import random
word_list = ["aardvark","baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)

place_holder = ""

for letter in chosen_word :
    place_holder += "_"
print (f"{place_holder}\n")



while lives > 0 :
    guess = input("guess a letter : ").lower()
    display = ""
    for letter in chosen_word :
        if letter == guess :
            display += letter
        else:
             display += "_"
             lives = lives - 1
    
    print (display)


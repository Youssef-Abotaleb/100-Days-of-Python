import random
word_list = ["aardvark","baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)

place_holder = ""

for letter in chosen_word :
    place_holder += "_"
print (f"{place_holder}\n")

game_over = False

correct_letters =[]

while not game_over :
    guess = input("guess a letter : ").lower()

    display = ""

    for letter in chosen_word :
        if letter == guess :
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
             display += "_"
    
    print (display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0 :
            game_over = True
            print("You Lose.")
        
    
   
    if "_" not in display:
        game_over = True
        print("You Win.")
    
    
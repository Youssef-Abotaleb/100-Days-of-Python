import random

pchoice = int (input("What do you choose ? Type 0 for rock, 1 for paper or 2 for scissors."))

cchoice = random.randint(0,2)

if pchoice == 0 and cchoice == 0 :
    print("You Chose rock and the computer chose rock as well Its a tie")
elif pchoice == 0 and cchoice == 1 :
    print("You Chose rock and the computer chose paper , The compuer wins")
elif pchoice == 0 and cchoice == 2: 
    print("You Chose rock and the computer chose scissors , YOU WIN!")
elif pchoice == 1 and cchoice == 0 :
    print("You Chose paper and the computer chose rock YOU WIN")
elif pchoice == 1 and cchoice == 1 :
    print("You Chose paper and the computer chose paper as well Its a tie")
elif pchoice == 1 and cchoice == 2 :
    print("You Chose paper and the computer chose scissors , the computer wins")
elif pchoice == 2 and cchoice == 0 :
    print("You Chose scissors and the computer chose rock, the computer wins")
elif pchoice == 2 and cchoice == 1 :
    print("You Chose scissors and the computer chose paper, YOU WIN")
elif pchoice == 2 and cchoice == 2 :
    print("You Chose scissors and the computer chose scissors as well Its a tie")
else :
    print("invalid input")


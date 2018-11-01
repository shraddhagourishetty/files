# Mon. Oct. 22nd class file example
# Go over this basic game, we will be creating a dice class for this

#standard imports
import random
import time

# create a basic dice game  - this should be understood - nothing new here...
def dice():
    player = random.randint(1, 6)
    print("You rolled " + str(player))

    computer = random.randint(1, 6)
    print("The computer rolls....")
    time.sleep(2)
    print("The computer has rolled a " + str(player))

    if player > computer:
        print("You win")  # basic if statement, win or loose
    elif player == computer:
        print("you tied")
    else:
        print("You lose")

    print("Quit? Y/N")    # alternate way to ask for continuation in fcn
    cont = input()  # we previously used an while  not quit or something similar.

    if cont == "Y" or cont == "y":
        exit()
    elif cont == "N" or cont == "n":
        pass
    else:
        print("I did not understand that. Playing again.")


# main loop - beginning proper programming, rather than on-offs
while True:
    print("Press return to roll your die.")
    roll = input()  #what is this doing? - put in a proper comment
    dice()  # calling our dice definition.
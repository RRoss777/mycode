#!/usr/bin/env python3

"""Alta3 Research | RRoss
- Using while, if, elif, else"""

rounds = 0
while True:
    rounds = rounds + 1
    print('Finish the movie title, "Monty Python\'s The Life of _______"')

    answer = input("Your guess--> ")

    if answer == 'Brian':
        print('Correct')
        break
    elif rounds==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")



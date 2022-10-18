#!/usr/bin/env python3

"""Alta3 Research | RRoss
Challenge: Lists, Input, Print, Variables"""

import random

def main():

    wordbank= ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif",
                 "Brent", "Cedric", "Chris",
                 "Cory", "Ebrima", "Franco",
                 "Greg", "Hoon", "Joey", "Jordan",
                 "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)
    #print(wordbank)

    #for original problem, num= int(input("Enter a number between 0 and 18. "))
    #for Bonus 2; set num variable to account for list lengths
    num= int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]

    print(f"Our fortunate student volunteer is {name}!")
    #output= (name + " always uses " + str( wordbank[2]) + " "  +  wordbank[1] + " to indent.")
    #print(output)

    #using both lists for variable data in a string
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    #for Bonus 1, choosing a random student name
    name = random.choice(tlgstudents)
    print(f"{name} is next!")

if __name__ == "__main__":
    
    main()

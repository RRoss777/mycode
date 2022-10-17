#!/usr/bin/env python3

wordbank= ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

wordbank.append(4)

#num= int(input("Pick a number between 0 and 18!"))
choice= int(input("Pick a number between 0 and 18!"))
student_name= tlgstudents[choice]

print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

#!/usr/bin/env python3

def main():

    #ask for user's name
    name=input("What is your name? ")

    #ask what day of the week it is
    dotw=input("What day of the week is it? ")

    #reply with greeting including username and day of the week
    greeting=("Hello " + name + "! Happy " + dotw + "!")
    print(greeting)

main()

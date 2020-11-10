# import packages to extend python (just like we extend sublime, or Atom, or VScode)
from random import randint

# [] => this is an array, an array is a special type of container that can hold multiple items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock", "paper", "scissors"]

# this is the player choice
player = input ("Choose rock, paper or scissors: ")

# this will be the AI choice -> a random pick from the choices array
computer = choices[randint(0, 2)]

# just to validate that i can make a choice

# print outputs whatever is in the round brackets -> in this case it outputs player to the command prompt window
print("user chose " + player)

# validate tgar the random choice worked for the AI
print("AI chose " + computer)

if (computer == player):
	print("tie")

elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose! eat dust!")
	else: 
		print("you win! lets go!")

elif (computer == "paper"):
	if (player == "rock"):
		print("you lose! eat dust!")
	else: 
		print("you win! lets go!")

elif (computer == "scissors"):
	if (player == "paper"):
		print("you lose! eat dust!")
	else: 
		print("you win! lets go!")
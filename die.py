
from random import randint 

class Dice:
	""" Attempt to model a DICE class"""
	def __init__(self, sides=6):
        	self.sides = sides
        	
        

	def roll_die(self):
        	print(randint(1, 6))
        

my_dice = Dice()

print(f"I'm gonna do the first die roll {my_dice.roll_die()}\n")

rolltime = 0 

while rolltime < 11:
    my_dice.roll_die()	
    rolltime += 1
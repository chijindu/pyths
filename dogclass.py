
class Dog:
	""" representing the Dog class """
	def __init__(self, name, age):
		"""Constructor"""
		self.name = name
		self.age = age


	def sit(self):
		"""Function Sit"""
		print(f"My dog {self.name} is now sitting")



	def roll(self):
		"""Function roll"""
		print(f"My dog {self.name} is now rolling")


	def bark(self):
		"""Function roll"""
		print(f"{self.name} Wooh! Wooh!! Wooh! ! !")

my_dog = Dog('Scamp', 18)

my_dog.roll()
my_dog.bark()
def bmi(ht, wt):
	""" Calculate the body mass Index  """

	bm = wt / ht 
	return bm


height = int(input("Enter your height in meters: "))

weight = int(input("Enter your weight in meters: "))


zondus = bmi(height, weight)

if zondus > 30:
	print("More Exercise needed friend")

else:
	print("All is well")
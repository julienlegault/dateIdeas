import random

free = ["Hammocking", "Hike", "Walk", "Movie Night", "New Conservation Land", "Geocashing", "Picnic", "Puzzle", "Online Quizzes", "Open House", "Game Night", "Bonfire", "Pool Party", "Workout", "Clean House", "Clean Car", "Play on a Playground", "Collect Shells at the Beach", "Fishing", "Learn Hebrew", "Play a Steam 2p Game"]
cheap = ["McDonalds", "Movies", "Cook Dessert", "Pie in the Sky", "Daily Brew", "Cosmic Canoli", "Museaum", "Bowling", "Mini Golf", "Thrift Store", "At-Home Spa", "Drive In", "See a Psychic", "Plymouth Plantation", "Ice Cream", "Coffee", "Build Something with Wood", "Zoo"]
moderate = ["Pickle Jar", "Seafood Sam", "Ciema Pub", "Cape Cod Mall", "Cheese Shop", "Nice Ass Museaum", "Hobby Shop", "Rock Clibming", "Amusement Park", "Manacure/Petacure", "Buy an Outfit for Eachother", "Try a new Ice Cream Spot", "Try a new Coffee Spot", "Escape Room"]
expensive = ["Waterstreet Kitchen", "Day Trip to Boston", "Julien's House", "Boat", "Vinyard", "Bleu", "Fisherman's View"]

arrayType = input("Enter f/c/m/e for price selection: ")
if(arrayType == 'f'):
	print("Your date is", random.choice(free))
elif(arrayType == 'c'):
	print("Your date is", random.choice(cheap))
elif(arrayType == 'm'):
	print("Your date is", random.choice(moderate))
elif(arrayType == 'e'):
	print("Your date is", random.choice(expensive))
else:
	print("Choose a real selection")

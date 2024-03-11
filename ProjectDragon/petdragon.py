# Pet Dragon

from random import randrange

class Dragon(object):
	"""---A Virtual Dragon---"""
	hyper_reduce = 3
	hyper_max = 10
	hyper_warning = 3
	hunger_reduce = 2
	hunger_max = 10
	hunger_warning = 3
	vocab = ['"Grrr"']
	color = "blue"

	#constructor

	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.hyper = randrange(self.hyper_max)
		self.hunger = randrange(self.hunger_max)
		self.vocab = self.vocab[:]

	def __clock_tick(self):
		self.hyper -= 1
		self.hunger -= 1

	@property
	def mood(self):
		if (self.hunger > self.hunger_warning) and self.hyper > self.hyper_warning:
			return "happy"
		elif self.hunger < self.hunger_warning:
			return"hungry"
		else:
			return "bored"

	def __str__(self):
		return "\nI'm" + self.name + "." "\nI feel " + self.mood() + "."

	def teach(self, word):
		self.vocab.append(word)
		self.__clock_tick()

	def talk(self):
		print("I am a " + self.color + " dragon.",
			"I feel " + self.mood(),
			" now.\n")
		self.__clock_tick()

	def feed(self):
		print("***nomnomnom*** \n Thank you!")
		meal = randrange(self.hunger, self.hunger_max)
		self.hunger += meal

		if self.hunger < 0:
			self.hunger = 0
			print("I'm still hungry!")
		elif self.hunger > self.hunger_max:
			self.hunger = self.hunger_max
			print("I'm full")
		self.__clock_tick()

	def play(self):
		print("Woohoo!")
		fun = randrange(self.hyper, self.hyper_max)
		self.hyper += fun
		if self.hyper < 0:
			self.hyper = 0
			print("I am bored")
		elif self.hyper > self.hyper_max:
			self.hyper = self.hyper_max
			print("Let's go burn some things down!")
		self.__clock_tick()

	def burn(self):
		print("We don't talk about Fight Club")

def main():
    dragon_name = input("What do you want to name your pet? ")
    # dragon_color = # refer to food choice

    myDragon = Dragon(dragon_name, Dragon.color)
  # add , color and when adding, make sure to change from . to dragon_color

    input(
        "Roar! I am " + dragon_name + ".\n"
        "\nPress enter to start. ")

    choice = None  # Initialize choice variable

    while choice != "0":
        print(
            """
            ***INTERACT WITH YOUR PET***

            1 - Feed your Dragon
            2 - Talk with your Dragon
            3 - Teach your Dragon a new word
            4 - Play with your Dragon
            5 - Burn down place of employment
            0 - Quit
            """)

        choice = input("Choice: ")

        if choice == "0":
            print("Good bye")
        elif choice == "1":
            myDragon.feed()
        elif choice == "2":
            myDragon.talk()
        elif choice == "3":
            new_word = input("What do you want to teach your pet to say?")
            myDragon.teach(new_word)
        elif choice == "4":
            myDragon.play()
        elif choice == "5":
        	myDragon.burn()
        else:
            print("Sorry, that isn't a valid option.")

if __name__ == "__main__":
    main()

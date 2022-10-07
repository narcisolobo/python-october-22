# from pet import Pet
from ninja import Ninja
from wolf import Wolf

# snoopy = Pet('Snoopy', "beagle", "Roll Over")
# charlie = Ninja("Charlie", "Brown", "Cookies", "Dog Food", snoopy)

# charlie.walk().feed().bathe()

# ghost = Wolf('Ghost')

# ghost.noise()

print('You will create a wolf!')
wolf_name = input('Name your wolf: ')
wolf = Wolf(wolf_name)

print(f'Your wolf\'s name is {wolf.name}, energy is: {wolf.energy}.')
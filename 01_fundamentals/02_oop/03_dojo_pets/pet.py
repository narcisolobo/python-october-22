class Pet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.energy = 100

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print('The pet is eating...')
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        print('The pet is playing...')
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print('Pet makes noise.')
        return self

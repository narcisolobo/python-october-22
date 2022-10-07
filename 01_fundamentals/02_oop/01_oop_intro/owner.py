class Owner:
    def __init__(self, first_name, last_name, email, age, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.pet = pet
    
    def walk(self):
        print('Walking...')
        return self
    
    def greet(self):
        print(f'Hi, I\'m {self.first_name}')
        return self

    def say_age(self):
        return self.age
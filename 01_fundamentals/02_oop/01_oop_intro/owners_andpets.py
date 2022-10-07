from owner import Owner
from pet import Pet

aspen = Pet('Aspen', 'Husky', 10)
lola = Owner('Lola', 'Russell', 'lola@russell.com', 22, aspen)

print(lola.pet.name)
lola.greet().greet()

age = lola.say_age()
print(age)
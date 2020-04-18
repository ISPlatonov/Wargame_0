from random import randint
class Warrior:
    health = 100
    name = 'Some person'
    def attack(self, person):
        try:
            person.health -= 20
            print(self.name + '(' +str(self.health) + ')', "attacked", person.name + '(' +  str(person.health) + ')')
        except:
            print("It has not a health")

per_1 = Warrior()
per_1.name = "Warrior_1"
per_2 = Warrior()
per_2.name = "Warrior_2"

while (per_1.health != 0) and (per_2.health != 0):
    n = randint(0, 10)
    if n % 2 == 0:
        per_2.attack(per_1)
    else:
        per_1.attack(per_2)
if per_1.health <= 0:
    print("Warrior_2 won!")
else:
    print("Warrior_1 won!")

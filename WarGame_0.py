from random import randint
class Warrior:
    def __init__(self, name_init):
        self.name = name_init
    health = 100
    def attack(self, person):
        try:
            person.health -= 20
            print(self.name + '(' +str(self.health) + ')', "attacked", person.name + '(' +  str(person.health) + ')')
        except:
            print("It has not a health")

per_1 = Warrior("Warrior_1")
per_2 = Warrior("Warrior_2")

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

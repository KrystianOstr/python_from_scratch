# class Monster:
    
#     def __init__(self, health, energy):
#         self.health = health
#         self.energy = energy
        
    
#     def attack(self, amount):
#         print(f'{amount} damage was dealt')
#         self.energy -= 20
        
#     def move(self):
#         print(f'Monster moved by 2 sqm')
        
        
# monster1 = Monster(90,40)
# monster1()

# monster1.attack(20)
# monster1.move()


# class Monster:
#     def __init__(self, func):
#         self.func = func
        
        
# class Attacks:
    
#     def bite(self):
#         print('bite')
    
#     def strike(self):
#         print('strike')
    
#     def slash(self):
#         print('slash')
    
#     def kick(self):
#         print('kick')
        
# monster1 = Monster(func = Attacks().bite)

# monster1.func()

# class Monster:
#     def __init__(self, health, energy):
#         self.health = health
#         self.energy = energy
        
#     def update_energy(self, amount):
#         self.energy += amount
            
#     def get_damage(self, amount):
#         self.health -= amount
            
# class Hero:
#     def __init__(self, damage, monster):
#         self.damage = damage
#         self.monster = monster
        
#     def attack(self):
#         self.monster.get_damage(self.damage)
        
         
            
# monster = Monster(health=100, energy=50)
# hero = Hero(damage=20, monster=monster)

# print(monster.health)

# hero.attack()
# hero.attack()
# hero.attack()

# print(monster.health)


class Monster:  
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        
    
    def attack(self, amount):
        print(f'{amount} damage was dealt')
        self.energy -= 20
        
    def move(self):
        print(f'Monster moved by 2 sqm')
        
        
class Shark(Monster):
    def __init__(self,speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed
        
    def bite(self):
        print('Bite')
        
    def move(self):
        print(f'Monster moved(swam) by {self.speed} sqm')
        
        
shark = Shark(speed = 120, health=100, energy=50)



class Scorpion(Monster):
    def __init__(self, health, energy, posion_damage):
        super().__init__(health, energy)
        self.posion_damage = posion_damage
        
    def attack(self):
        print('Dealt posion_damage')
        
        
scorpion = Scorpion(100, 50, 40)


scorpion.attack()
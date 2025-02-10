class Monster():
    
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        
    def __janusz__(self):
        print('dsadsadsa')
    
    def attack(self, amount):
        print(f'{amount} damage was dealt')
        self.energy -= 20
        
    def move(self):
        print(f'Monster moved by 2 sqm')
        
        
monster1 = Monster(90,40)
monster1()

monster1.attack(20)
monster1.move()

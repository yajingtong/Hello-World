import random

class Agent():
    
    def __init__(self, environment):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
    
    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
     




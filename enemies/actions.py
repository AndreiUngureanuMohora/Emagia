from random import randint

class Enemy: 
    def resetStats(self):
        self.stats['health'] = randint(60, 90)
        self.remaining_health = self.stats['health']
        self.stats['strength'] = randint(60, 90)
        self.stats['defence'] = randint(40, 60)
        self.stats['speed'] = randint(40, 60)
        self.stats['luck'] = randint(25, 40)
        self.stats['alive'] = True
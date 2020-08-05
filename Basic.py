from random import randint

class Basic: 
    def takeDamage(self, damage_received):
        self.remaining_health = self.remaining_health - damage_received

        if self.remaining_health <= 0:
            self.stats['alive'] = False

    def dealDamage(self, enemyDefence):
        return self.stats['strength'] - enemyDefence

    def checkSpeed(self, enemy):
        if(self.stats['speed'] > enemy.stats['speed']):
            return True
        elif(self.stats['speed'] == enemy.stats['speed']):
            if(self.stats['luck'] > enemy.stats['luck']):
                return True
        return False

    def testLuck(luck):
        return randint(0, 100) < luck
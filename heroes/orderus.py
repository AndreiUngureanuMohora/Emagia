from random import randint

class Orderus:

    stats = {
        'name': "Orderus",
        'health': randint(70, 100),
        'strength': randint(70, 80),
        'defence': randint(45, 55),
        'speed': randint(40, 50),
        'luck': randint(10, 30),
        'alive': True,
        'used_rapid_strike' : False,
        'rapid_strike_chance': 10,
        'magic_shield_chance': 20
    }

    remaining_health = stats['health']

    def rapidstrike(self):
        self.stats['used_rapid_strike'] = True

    def magicShield(damage_received):
        return damage_received / 2
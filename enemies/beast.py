from random import randint


class Beast:

    stats = {
        'name': "Beast",
        'health': randint(60, 90),
        'strength': randint(60, 90),
        'defence': randint(40, 60),
        'speed': randint(40, 60),
        'luck': randint(25, 40),
        'alive': True,
    }

    remaining_health = stats['health']
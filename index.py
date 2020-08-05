from heroes.orderus import Orderus
from enemies.beast import Beast

from heroes.actions import Hero #actions that only affect heroes
from enemies.actions import Enemy #actions that only affect enemies

from Basic import Basic #actions that affect both

hero = Orderus # we can change the hero here
numberOfBattles = 4
currentBattle = 1

while currentBattle < numberOfBattles and hero.stats['alive']:
    model = hero
    enemyModel = Beast # we can change the enemy here

    if enemyModel.stats['alive'] == False:
        Hero.resetStats(model)
        Enemy.resetStats(enemyModel)

    print(hero.stats['name'],'is fighting', enemyModel.stats['name'], currentBattle)

    if(Basic.checkSpeed(model, enemyModel) == False):
        model,enemyModel = enemyModel,model

    print(model.stats['name'], 'gets to attack first')
    
    while(model.stats['alive'] and enemyModel.stats['alive']):
        # offensive part starts here #
        amountOfDamage = Basic.dealDamage(model, enemyModel.stats['defence'])

        if(enemyModel == Orderus and Basic.testLuck(enemyModel.stats['magic_shield_chance'])):
            amountOfDamage = enemyModel.magicShield(amountOfDamage)
            print(enemyModel.stats['name'], 'uses Magic Shield to block', amountOfDamage, 'damage')

        if(Basic.testLuck(enemyModel.stats['luck'])):
            amountOfDamage == 0

        # offensive part ends here #

        # defensive part starts here #

        Basic.takeDamage(enemyModel, amountOfDamage)

        print(model.stats['name'], 'dealt', amountOfDamage, 'damage')

        if(model == Orderus and model.stats['used_rapid_strike'] == False): #this checks to see if rapid strike can be performed
            if(Basic.testLuck(model.stats['rapid_strike_chance'])):
                model.rapidstrike(model)
                print(model.stats['name'], 'uses Rapid Strike to attack again')
                continue
        elif(model == Orderus):
            model.stats['used_rapid_strike'] == False

        # defensive part ends here #

        if(model.stats['alive'] and enemyModel.stats['alive']):
            print(model.stats['name'], 'has:', model.remaining_health,'health')
            print(enemyModel.stats['name'], 'has:', enemyModel.remaining_health, 'health')

            model,enemyModel = enemyModel,model #here we change the combatants

    if(model.stats['alive']):
        print('The winner is:', model.stats['name'], '\n')
    else:
        print('The winner is:', enemyModel.stats['name'], '\n')

    currentBattle+= 1

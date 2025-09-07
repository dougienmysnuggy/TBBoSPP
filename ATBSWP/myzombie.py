import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        self.name = name
        
    def turn(self, gamesState):
        dice_roll_results = zombiedice.roll() # first roll
        # retirms keys 'brains', 'shotgun', 'footsteps' with values
        # for # of times rolled. 'rolls' key has a tuple (color, result)
        
        
        #This bot goes until at least 10 brains
        '''
        brains = 0
        shotguns = 0
        while dice_roll_results:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            if brains < 10 or shotguns >= 3:
                break
            else:
                dice_roll_results = zombiedice.roll()
        '''
        
        #This bot randomly chooses whether to roll again or not
        '''
        brains = 0
        shotguns = 0
        while dice_roll_results:
            brains += dice_roll_results['brains']    
            shotguns += dice_roll_results['shotgun']
            if random.randint(0, 1) == 1: #roll again
                dice_roll_results = zombiedice.roll()
            else:
                break
        '''
        
        #This bot will play until it gets 2 shotguns, but only if he has at least 5 brains
        '''
        brains = 0
        shotguns = 0
        while dice_roll_results:
            brains += dice_roll_results['brains']
            shotguns += dice_roll_results['shotgun']
            if shotguns >= 3:
                break
            if brains < 5 or shotguns < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break
        ''' 
        
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name = 'random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name = 'until leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'stops at 2 shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'stops at 1 shotgun', minShotguns=1),
    MyZombie(name='Wesley'),
)

#zombiedice.runWebGui(zombies=zombies, numGames=1000)
zombiedice.runTournament(zombies=zombies, numGames=1000)
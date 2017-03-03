'''
dice_game_class.py - Python Class that will simulate the rolling of
a pair of dice.
'''

import die_class

class Game:

    def __init__(self, num_players):
        '''Constructor that will set the number of
players as an attribute call num_players and initialize
two instances of Dice
'''
        # initialize attribute num_players
        self.num_players = num_players
        # create instances of Dice objects
        # When one class has an instance of another class
        # within it, this is called a "has-a" relationship
        # or also called a "containment" relationship
        self.die_1 = die_class.Die()
        self.die_2 = die_class.Die()

    def PlayGame(self):
        '''Method that will loop over the number of players
and play the game for those players.
'''
        # create class attribute that will hold
        # the scores (list of lists) for all players
        self.scores = []
        for i, player in enumerate(range(self.num_players)):
            # if enter is pressed then roll for the player
            if not raw_input('Player ' + str(i + 1) + ' press enter to roll'):
                self.scores.append(self.Roll())
            else:
                print 'Ok, thanks for playing'
        
    def Roll(self):
        '''Return a list that contains random roll of the dice.
'''
        return [self.die_1.RollDie(), self.die_2.RollDie()]
            
    def GetTotal(self):
        '''Return the total of two dice."
'''

        # list attribute that will contain the total of both dice
        # for each player
        self.player_totals = []
        #print self.scores
        for i, players_result in enumerate(self.scores):
            self.player_totals.append([sum(players_result), i + 1])
        #print self.player_totals
        
    def DetermineWinner(self):
        '''Method that will determine who is the winner
by sorting list of lists in reverse order.
'''
        self.sorted_list = sorted(self.player_totals, reverse=True)
        #print self.sorted_list

    def PrintWinners(self):
        '''Method that will loop over sorted_list
and print out the players from best score to worse.
'''
        print 'The scores descending are:\n'
        for i, player_result in enumerate(self.sorted_list):
            print 'Player',player_result[1],'has score of',player_result[0]
        
        

def StartGame():
    '''Program function that will ask for the number of players
and create an instance of Game and call methods PlayGame, GetTotal,
and DetermineWinner.
'''

    players = raw_input('Enter the number of players:\n')

    if players:
        try:
            int_players = int(players)
        except:
            ValueError
            print 'You must enter an integer number of players:\n'
        else:
            if int_players >= 1:
                game = Game(int_players)
                game.PlayGame()
    game.GetTotal()
    game.DetermineWinner()
    game.PrintWinners()

if __name__=='__main__':
    StartGame()

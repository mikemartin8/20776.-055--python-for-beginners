'''
lab_10_exercises_num_2_answer.py
'''

import random_module_randrange_function_as_module as rmrfam

PLAYER_1_RESULTS = []
PLAYER_2_RESULTS = []

def AskNumberOfTurns():

    while True:
        num_turns = raw_input('Input the number of turns for both players:\n')
        try:
            int_num_turns = int(num_turns)
            return int_num_turns
        except:
            print 'The number of turns input is not valid'
            continue
        

def PlayGame(num_turns):

    for turn in range(num_turns):

        player_1_result = rmrfam.TossCoins()
        player_2_result = rmrfam.TossCoins()

        PLAYER_1_RESULTS.append(CalcPoints(player_1_result))
        PLAYER_2_RESULTS.append(CalcPoints(player_2_result))


def CalcPoints(result):

    if result == True:
        return 2
    else:
        return 1

def PrintResults():

    player_1_total = TotalResults(PLAYER_1_RESULTS)
    player_2_total = TotalResults(PLAYER_2_RESULTS)

    print 'Total points for player 1 is:',player_1_total
    print 'Total points for player 2 is:',player_2_total

    if player_1_total > player_2_total:
        game_result = 'Player 1 wins!'
    elif player_1_total < player_2_total:
        game_result = 'Player 2 wins!'
    else:
        game_result = 'It is a tie!'

    print game_result
    

def TotalResults(results_list):

    total = 0
    
    for result in results_list:
        total = total + result

    return total
    
        


if __name__=='__main__':
    number_of_turns = AskNumberOfTurns()
    PlayGame(number_of_turns)
    PrintResults()

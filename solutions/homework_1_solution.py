'''
homework_1_solution.py
'''

#  General requirements with point values:
#  Points:                           pts. off if corrected       pts. off if not corrected
#  1.  Violation of style guide                      0                            5
#  2.  Very Confusing Code                           0                            5
#  3.  Ask for job title                             1                            2
#  4.  Ask for hourly wage                           1                            2
#  5.  Ask for money at retirement                   1                            2
#  6.  take float (or int) of hourly wage            1                            2
#  7.  take float (or int) of retirement money       1                            2
#  8.  try except around hourly wage                 2                            4
#  9.  try except around retirement money            2                            4
#  10.  Calculate annual wage                        1                            2
#  11.  Calc. num years to save                      1                            2
#  12.  Calc. num years even or odd                  1                            3
#  13.  Explain even/odd output                      1                            2
#  14.  2nd try except inside 1st try except else    1                            2
#  15.  Main calcs and output in 2nd else            1                            2



job_title = raw_input('What is the title of your dream job ')

hourly_wage = raw_input('What is your desired hourly wage? ')

try:
    float_hourly_wage = float(hourly_wage)
except ValueError:
    print '''The hourly wage you input is not a valid dollars and cents value
    please run the program again'''
else:
    retirement_money = raw_input('How much money will you need at retirement? ')

    try:
        float_retirement_money = float(retirement_money)
    except ValueError:
        print '''The value you input for retirment money is not valid, please run the proram
        again'''
    else:

        # Determine the number of years they will have to work to
        # save up their retirement dollar value assuming their only
        # source of income was their paycheck

        weekly_wage = float_hourly_wage * 40
        #  will also accept 48 weeks
        yearly_income = weekly_wage * 52

        num_years_to_save = float_retirement_money / yearly_income

        print 'The number of years you will have to save to have',float_retirement_money,'is'\
              ,num_years_to_save,'years'


        # determine if the number of years they need to save is an even or odd number

        even_or_odd = int(num_years_to_save) % 2

        print 'Modulus of the number of years to save is',even_or_odd,'.  If the value is 0 then it is'\
            ' even, if it is 1 then it is odd number of years'

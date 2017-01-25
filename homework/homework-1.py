## Michael Martin
## 1/21/2017
## Homework #1

## Ask the user what their dream job is and display it back to the user
dream_job = raw_input("What is your dream job? \n")
print "Your dream job would be being a", dream_job

## Ask what the hourly wage is he/she wishes to earn and display it back
hourly_wage = raw_input("What is the hourly wage you wish to earn?\n")

## Confirming that the user input a dollar amount as only a number to
## two decimal places
try:
    hourly = float(hourly_wage)
except ValueError:
    print "The hourly wage you entered (", hourly_wage, ") must be a rational number only."
else:
    ## Commenting to the user what their pre-tax salary will be
    num_paid_weeks =        52
    num_hours_per_week =    40
    salary =                int(num_paid_weeks) * int(num_hours_per_week) * int(hourly_wage)
    print "As a",dream_job,", making $", hourly,", you will make $",salary,"per year, before taxes."

    ## Asking about their desired cash savings desires at retirement
    retirement_cash = raw_input("How much cash would you like to have at retirement?")

    ## Confirming that the user input a dollar amount as only a number to
    ## two decimal places
    try:
        retirement = float(retirement_cash)
    except ValueError:
        print "You desired retirement amount (", retirement, ") must be a rational number only."
    else:
        print "Your desired retirement amount is $", retirement,"."

        ## Do that math to determine how many years the user has to work to acheive the retirement amount. Tell the user.
        try:
            working_years = round(retirement/salary,2)
        except ZeroDivisionError:
            print "Error: You cannot divide by zero!!"
        else:
            print "As a",dream_job,"making",salary,"per year, you will need to work for",working_years,"years."

            ## Use the modulo function (%) to determine if the numbers of years he/she has to work is odd or even
            working_years

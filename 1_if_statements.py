# If statements

# Syntax
# if (condition) :
#       # indent for code block

weather = 'rainy'

assertion =  (weather == 'sunny')
print(assertion)

#--------------#

if weather == 'sunny':
    print("Let's have a picnic")

torch_lit = True

if torch_lit:
    print("My path is clear")

# If checks a condition/assertion and if it's true will execute a defined code block

# COMPOUND CONDITIONAL STATEMENTS using 'and' and 'or' logical operators

#--- and : requires that both conditions are true in order to execute our code block

gold_coins = 10
silver_coins = 50

if (gold_coins > 5) and (silver_coins > 30):
    print("Enough to buy the magic potion!")


#--- or : Requires that at least one condition needs to be True in order to execute our code block

day = 'monday'

if day == 'saturday' or day == 'sunday': # As long as the day is eother saturday OR sunday
    print("Yaaaaaayy it's the weekend!") #run our code block


#--- Using 'and' and 'or' TOGETHER

caffinated = False
prepared_lvl = 11
confidence = 90

# How ready am I to teach?

#       False        True                      True
if (caffinated and prepared_lvl > 6) or (confidence > 80):
    print("I'M READYYYYYYYY to teach!!!")


dressed = True
weather = 'sunny'
num_of_friends = 4

#   True                True                  True
if (dressed and num_of_friends >= 3) or (weather == 'sunny'):
    print("Let's go to the beach!!!")

# print(dressed and num_of_friends >= 3)
# print(weather == 'sunny')

#--- Using the 'not' operator

# By incorporating 'not' our if statement runs off of False conditions

busy = False
#if not True

#if False: 
#    run code
if not busy:
    print("Aaaahh time to relax!!")

time = 8.30
#        False
if not (time < 7):
    print("I should be awake!")

# There are always ways of getting around using not!
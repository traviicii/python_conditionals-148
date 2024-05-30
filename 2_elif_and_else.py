# If statement are our original condition
# elif allows us to chain on additional conditions/assertions, with their own corresponding code blocks

# The flow of the if/elif chain reads from the top down, and as soon as a conditional statement evaluates to True, that code block is ran and the rest of the conditions are skipped

money = 15

if money >= 50:
    print("We can have a steak dinner")
elif money >= 20:
    print("Italian sounds like a good choice!")
elif money >= 10:
    print("Let's grab Chipotle!")

#------------#
# Else statements are essentially a default condition. 
# They don't have a specific condition of their own, but if none of the other conditions evaluate to True, then the else block will run its code

money = 8

if money >= 50:
    print('Lets have a nice steak dinner')
elif money >= 20:
    print('Italian sounds like a good choice!')
elif money >= 10:
    print('Lets grab chipotle!')
else:
    print("I probably should just cook at home :(")
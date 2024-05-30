# Nested if statements

# in  python we can have nested if's, or if statements inside if statement

# Activity of the day

weather = 'sunny'
friends = 5

if weather == 'sunny': # Outer condition
    # Inner if's
    if friends <= 6:
        print("Let's play volleyball!")
    elif friends == 5:
        print("Let's play frisbee")
    else:
        if friends == 1:
            print("I think I'll play some golf... all by my lonesome :(")
        elif friends < 5:
            print("The", friends, 'of us, should play golf!')
else:
    print("Let's go to the movies!")

print("Now we're here")


# if friends >= 6:
#     print("Let's play volleyball!")
# elif friends == 5:
#     print("Let's play frisbee")
# else:
#     if friends == 1:
#         print("I think I'll play some golf... all by my lonesome :(")
#     else:
#         print("The", friends, 'of us, should play golf!')
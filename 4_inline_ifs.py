# Inline if statements (ternary operators) are simply a way to write if statements in a single line

# syntax
# <True return> if <condition> else <False return>

# Why? Allows us to have concise conditionals within a single line

candy_jar = 'empty'

#       <True return>    if    <condition>       else    <False return>
print("It's candy time!" if candy_jar == 'full' else "Time to hit up Mr. Wonka")

if candy_jar == 'full':
    print("It's candy time!")
else:
    print("Time to hit up Mr. Wonka")


# ternary operator with 'and'

candy_jar = 'empty'
sweet_tooth = True

print("It's candy time!" if candy_jar == 'full' and sweet_tooth else 'Who needs candy anyway?')
# print(candy_jar == 'full' and sweet_tooth)

# statement = "It's candy time!" if candy_jar == 'full' and sweet_tooth else 'Who needs candy anyway?'

# print(statement)

# ternary operator with 'or'

day = 'tuesday'

print("It's the weekend") if (day == "saturday") or (day == "sunday") else print("BOOOOOOOO it's not the weekend!")
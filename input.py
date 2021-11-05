# Checks if the user's answer can be used by the determineReply() 
# function, and if it cannot provides an error.
def get_reply(user_input):
    if user_input.isdigit():
        user_input_int = int(user_input)
        return determine_reply(user_input_int)
    else:
        return 'Sorry, I don\'t understand your answer. I was looking for a number, not a string.'

# Determines the correct reply
def determine_reply(user_input_int):
    if user_input_int > 2:
        return 'Wow, that\'s a lot of coffee!'
    elif user_input_int == 0:
        return 'Should we go grab a coffee? I could use one too.'
    else:
        return 'Sounds like the right amount of coffee to start the day.'

# Ask for user input
user_coffee_input = input('How many cups of coffee have you had today? ')

# Process the answer to get the right reply, and print that reply
reply = get_reply(user_coffee_input)
print(reply)

"""
# practising input() with conditional statements
user_coffee_input = input('How many cups of coffee have you had today? ')
user_coffee_input = int (user_coffee_input)

if user_coffee_input > 2:
    print('Wow, that\'s a lot of coffee!')
elif user_coffee_input == 0:
    print('Should we go grab a coffee? I could use one too.')
else:
    print('Sounds like the right amount of coffee to start the day.')
"""
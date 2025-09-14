"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
# Give instructions to users at the beginning
print('Think of a number between 1 and 100. I will try to guess it.')
print('After each guess, tell me if it is too high, too low, or correct. ')

# Provide the boundaries for users
lowest_num = 1 # the lowest possible number in this game
highest_num = 100 # the highest possible number in this game

# Start guessing untill find the correct answer
while True:
    # The computer uses dichonomy to find the number; 
    guess = (lowest_num + highest_num)//2 # "//" can make sure that the number is an integer

    # To present the guess to the user and obtain the feedback; use the f-string to insert the guess number
    feedback = input(f"Is your number = {guess}? (high/low/correct)")

    # If the guess is too high, 
    if feedback == "high":
        highest_num = guess - 1 # the boundary of the highest number is reduced one from the current guess
    
    # If the guess is too low, 
    elif feedback == "low":
        lowest_num = guess + 1 # the boundary of the lowest number is added one from the current lowest guess
    
    # If the guess is correct, 
    elif feedback == "correct":
        print(f"Found it! The number you guess was {guess}.") # print the success sentence and terminate the program; use the f-string to insert the correct number
        break
    
    # If the input is anything other than the feedback (such as high, low, incorrect), Inform the user that the input is invalid
    else:
        print("Invalid input. Please print 'high', 'low', or 'correct'.")
        

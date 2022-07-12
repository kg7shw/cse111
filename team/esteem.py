# I feel that I am a person of worth, at least on an equal plane with others.
# I feel that I have a number of good qualities.
# All in all, I am inclined to feel that I am a failure.
# I am able to do things as well as most other people.
# I feel I do not have much to be proud of.
# I take a positive attitude toward myself.
# On the whole, I am satisfied with myself.
# I wish I could have more respect for myself.
# I certainly feel useless at times.
# At times I think I am no good at all.

def main():

    print('This program is an implementation of the Rosenberg')
    print('Self-Esteem Scale. This program will show you ten')
    print('statements that you could possibly apply to yourself.')
    print('Please rate how much you agree with each of the')
    print('statements by responding with one of these four letters:')

    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()
    total = 0
    # Question #1
    score = ask_positive("I feel that I am a person of worth, at least on an equal plane with others. Enter D, d, a, or A:")
    total += score
    # Question #2
    score = ask_positive('I feel that I have a number of good qualities. Enter D, d, a, or A: ')
    total += score
    # Question #3
    score = ask_negative('All in all, I am inclined to feel that I am a failure. Enter D, d, a, or A: ')
    total += score
    # Question #4
    score = ask_positive('I am able to do things as well as most other people. Enter D, d, a, or A: ')
    total += score
    # Question #5
    score = ask_negative('I feel I do not have much to be proud of. Enter D, d, a, or A: ')
    total += score
    # Question #6
    score = ask_positive('I take a positive attitude toward myself. Enter D, d, a, or A: ')
    total += score
    # Question #7
    score = ask_positive('On the whole, I am satisfied with myself. Enter D, d, a, or A: ')
    total += score
    # Question #8
    score = ask_negative('I wish I could have more respect for myself. Enter D, d, a, or A: ')
    total += score
    # Question #9
    score = ask_negative('I certainly feel useless at times. Enter D, d, a, or A: ')
    total += score
    # Question #10
    score = ask_negative('At times I think I am no good at all. Enter D, d, a, or A: ')
    total += score


    print(f"Your score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")



def ask_positive(question):
    response = input(question)

    if response == "D":
        score = 0
    elif response == "d":
        score = 1
    elif response == "a":
        score = 2
    elif response == "A":
        score = 3

    return score


def ask_negative(question):
    response = input(question)

    if response == "D":
        score = 3
    elif response == "d":
        score = 2
    elif response == "a":
        score = 1
    elif response == "A":
        score = 0

    return score






















main()
import time
import math
import random


# Unfortunately I omitted the timer to limit the time a user has to enter an
# input as I could not find a solution I could understand and would not impact the flow of the game for the user


def show_menu():
    # This method is to show the menu and where the user can start the game or close the application

    exit_application = False
    greeting_message = "\n\nWelcome to MATH QUIZ\n"
    menu_options_message = ("please section one of the following\n"
                            "S) Start game\n"
                            "E) Exit application\n")
    invalid_selection_message = "The option you selected is not available\n"

    print(greeting_message)

    while exit_application is False:
        user_selection = input(menu_options_message)

        match user_selection.upper():
            case "S":
                run_game()
            case "E":
                exit_application = True
            case _:
                print(invalid_selection_message)


def run_game():
    # This method is the main functionality  of the game, it uses a for loop to determine the number of questions to ask
    # The time to respond is then collected for scoring
    # The users answer is then checked before incrementing the score and correct answer count
    start_message = "Starting game\n"
    wrong_answer_message = "incorrect\n"
    right_answer_message = "correct\n"
    total_score_message = "Score: %d\n\n"
    total_answered_message = "You answered %d questions correctly"

    correct_answer_count = 0
    user_score = 0

    print(start_message)
    for i in range(0, 10):
        question_and_answer = generate_question_and_answer()

        start_time = time.time()
        user_answer = get_user_answer(question_and_answer[0])
        end_time = time.time()

        if user_answer == question_and_answer[1]:
            print(right_answer_message)
            correct_answer_count += 1
            user_score += calculate_question_score(start_time, end_time)
        else:
            print(wrong_answer_message)

    print(total_answered_message % correct_answer_count)
    print(total_score_message % user_score)


def get_user_answer(question):
    # gets the user input and validates that the user entered an integer

    try:
        user_answer = int(input(question))
    except ValueError:
        return -1
    return user_answer


def calculate_question_score(start_time, end_time):
    # This method is used to calculate how many points to give the user for a correct answer
    math.floor(end_time)
    math.floor(start_time)
    time_taken = end_time - start_time
    if time_taken > 10:
        return 0
    else:
        return 10 - time_taken


def generate_question_and_answer():
    # This method uses two random integers to create a question in the format below
    # and returns the Q&A in a list

    question_format = "%d + %d = "
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    return [question_format % (number1, number2), number1 + number2]


show_menu()

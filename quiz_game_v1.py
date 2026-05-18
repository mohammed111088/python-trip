import random
import time

questions = {

    "What is the capital of Saudi Arabia?": {
        "choices": {
            "A": "Riyadh",
            "B": "Jeddah",
            "C": "Dammam",
            "D": "Mecca"
        },
        "answer": "A"
    },

    "What is 5 + 5?": {
        "choices": {
            "A": "8",
            "B": "10",
            "C": "15",
            "D": "20"
        },
        "answer": "B"
    },

    "What color is the sky?": {
        "choices": {
            "A": "Green",
            "B": "Blue",
            "C": "Red",
            "D": "Yellow"
        },
        "answer": "B"
    },

    "How many days are in a week?": {
        "choices": {
            "A": "5",
            "B": "6",
            "C": "7",
            "D": "8"
        },
        "answer": "C"
    },

    "What is the capital of China?": {
        "choices": {
            "A": "Shanghai",
            "B": "Beijing",
            "C": "Guangzhou",
            "D": "Shenzhen"
        },
        "answer": "B"
    },

    "Which animal says meow?": {
        "choices": {
            "A": "Dog",
            "B": "Cow",
            "C": "Cat",
            "D": "Lion"
        },
        "answer": "C"
    },

    "What is the largest planet?": {
        "choices": {
            "A": "Earth",
            "B": "Mars",
            "C": "Jupiter",
            "D": "Venus"
        },
        "answer": "C"
    },

    "How many hours are in a day?": {
        "choices": {
            "A": "12",
            "B": "24",
            "C": "48",
            "D": "60"
        },
        "answer": "B"
    },

    "What is the opposite of hot?": {
        "choices": {
            "A": "Warm",
            "B": "Cold",
            "C": "Big",
            "D": "Fast"
        },
        "answer": "B"
    },

    "Which language are we using?": {
        "choices": {
            "A": "Java",
            "B": "C++",
            "C": "Python",
            "D": "Swift"
        },
        "answer": "C"
    }

}

print("==========\nWELCOME TO PLAY\n============")


def choose_difficulty():

    user_choose = input("Choose level: easy, normal, hard: ").lower()

    if user_choose == "easy":
        return 3
    elif user_choose == "normal":
        return 5
    elif user_choose == "hard":
        return 10


def show_question(q):

    print(q)

    for key, value in questions[q]["choices"].items():
        print(f"{key}) {value}")


def get_answer():

    user_answer = input("Your answer: ").upper()
    return user_answer


def check_answer(user_answer, correct_answer):

    if user_answer == correct_answer:
        return True
    else:
        return False


def show_result(is_correct):

    if is_correct:
        print("Correct!")
    else:
        print("Wrong")


def start_game():

    while True:

        score = 0

        question_count = choose_difficulty()

        random_question = random.sample(list(questions.keys()), question_count)

        for q in random_question:

            show_question(q)

            start_time = time.time()

            user_answer = get_answer()

            end_time = time.time()

            total_time = end_time - start_time

            if total_time > 10:
                print("Too late!")
                continue

            is_correct = check_answer(user_answer, questions[q]["answer"])

            show_result(is_correct)

            if is_correct:
                score += 1
        print(f"Final Score: {score}/{question_count}")
        again = input("play again? yes/no: ").lower()

        if again != "yes":
            print("Goodbye")
            break


start_game()

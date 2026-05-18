import  random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def game(user, computer):
    global user_score
    global computer_score
    print(f"You chose {user}, computer chose {computer}.")
    if user == computer:
        print(f"Both players selected{user}. it's a tie!")
    elif user == "rock":
        if computer == "scissors":
            user_score += 1
            print(f"Rock smashes scissors! You scored 1 point. Your score is {user_score}, computer score is {computer_score}\n")
        else:
            computer_score += 1
            print(f"Paper covers rock! Computer scored 1 point. You score is {user_score}, computer score is {computer_score}\n")
    elif user == "paper":
        if computer == "rock":
            user_score += 1
            print(f"Paper covers rock! You scored 1 point. You score is {user_score}, computer score is {computer_score}\n")
        else:
            computer_score += 1
            print(f"Scissors cuts paper! You scored 1 point. You score is {user_score}, computer score is {computer_score}\n")
    elif user == "scissors":
        if computer == "paper":
            print(f"Scissors cuts paper! You scored 1 point. You score is {user_score}, computer score is {computer_score}\n")
        else:
            computer_score += 1
            print(f"Rock smashes scissors! Computer scored 1 point. You score is {user_score}, computer score is {computer_score}\n")


while True:
    if user_score == 10:
        print("="*30, "\nYour score reached 10. YOU WIN!\n", "="*30)
        exit()
    elif computer_score == 10:
        print("=" * 30, "\nComputer score reached 10. COMPUTER WIN!\n", "=" * 30)
        exit()

    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)

    if user_choice == "quitgame":
        print("FINISH")
        exit()
    elif not user_choice in choices:
        print("You chose a wrong choice, please try again")
    else:
        game(user_choice, computer_choice)
from trivia_questions import questions
import random


def main():
    print("Welcome to the Programming Trivia (Provia) :)")
    while True:
        start()
        while True:
            restart = input("Would you like to play again? (y/n): ").strip().lower()
            if restart in ("yes", "y", "no", "n"):
                break
            print("Did not get that; please type [yes/y] or [no/n].\n")

        # Decide whether to continue or exit
        if restart in ("no", "n"):
            print("See you later!")
            break


def start():
    score = 0
    question_amount = get_valid_int_input("the amount of questions you wish to answer")
    total_questions = min(question_amount, len(questions))
    selected_questions = random.sample(questions, k=total_questions)
    for q_num, q in enumerate(selected_questions, start=1):
        while True:
            print(f'[{q_num}] {q["question"]}')
            for idx, option in enumerate(q["options"]):
                print(f" ({chr(97+idx)}) {option}")
                # i += 1
            print()
            user_answer = get_input("your answer").lower().strip()

            valid_letters = [chr(97 + i) for i in range(len(q["options"]))]
            if user_answer in valid_letters:
                index = ord(user_answer) - 97
                selected_answer = q["options"][index]
                break
            print("Input a valid option from (a) - (d)\n")
        if selected_answer == q["answer"]:
            print("correct!")
            print()
            score += 1
        else:
            print("Wrong!")
            print(f'Answer: {q["answer"]}')
            print()

    print(f"You scored:  {score}/{total_questions}")


def get_input(text):
    return input(f"Enter {text}: ")


def get_valid_int_input(text):
    while True:
        try:
            return int(get_input(text))
        except ValueError:
            print("Input a valid integer")


if __name__ == "__main__":
    main()

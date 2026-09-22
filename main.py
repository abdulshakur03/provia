from trivia_questions import questions
import random


def main():
    random.shuffle(questions)
    # question_num = 1
    score = 0
    total_questions = min(10, len(questions))
    selected_questions = questions[:total_questions]
    for q_num, q in enumerate(selected_questions, start=1):
        while True:
            print(f'[{q_num}] {q["question"]}')
            # i = 0
            for idx, option in enumerate(q["options"]):
                print(f" ({chr(97+idx)}) {option}")
                # i += 1
            print()
            user_answer = get_input("your answer").lower().strip()
            index = ord(user_answer) - 97
            selected_answer = q["options"][index]
            print()
            if user_answer in ("a", "b", "c", "d"):
                match user_answer:
                    case "a":
                        user_answer = selected_answer
                    case "b":
                        user_answer = selected_answer
                    case "c":
                        user_answer = selected_answer
                    case "d":
                        user_answer = selected_answer
                if user_answer == q["answer"]:
                    print("correct!")
                    print()
                    score += 1
                else:
                    print("Wrong!")
                    print(f'Answer: {q["answer"]}')
                    print()
                break
            else:
                print("Input a valid option\n")

    print(f"You scored:  {score}/{total_questions}")


def get_input(text):
    return input(f"Enter {text}: ")


if __name__ == "__main__":
    main()

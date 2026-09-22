from trivia_questions import questions
import random


def main():
    random.shuffle(questions)
    question_num = 1
    score = 0
    total_question = 10
    for i in range(total_question):
        if i >= len(questions):
            print("only range 1-100")
            break
        question = questions[i]
        for key, value in question.items():
            if key == "question":
                while True:
                    print(f'[{question_num}] {question["question"]}')
                    i = 0
                    for option in question["options"]:
                        print(f" ({chr(97+i)}) {option}")
                        i += 1
                    print()
                    user_answer = get_input("your answer")
                    print()
                    if user_answer in ("a", "b", "c", "d"):
                        match user_answer:
                            case "a":
                                user_answer = question["options"][0]
                            case "b":
                                user_answer = question["options"][1]
                            case "c":
                                user_answer = question["options"][2]
                            case "d":
                                user_answer = question["options"][3]
                        if user_answer == question["answer"]:
                            print("correct!")
                            print()
                            score += 1
                        else:
                            print("Wrong!")
                            print(f'Answer: {question["answer"]}')
                            print()
                        break
                    else:
                        print("Input a valid option\n")

        question_num += 1
    print(f"You scored:  {score}/{total_question}")


def get_input(text):
    return input(f"Enter {text}: ")


if __name__ == "__main__":
    main()

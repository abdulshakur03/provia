from test_trivia_questions import questions
import random


def main():
    random.shuffle(questions)
    question_num = 1
    score = 0
    for question in questions:
        # question = questions[i]
        # print(f"question: {question}")
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
                        print("usy:", user_answer)
                        if user_answer == question["answer"]:
                            score += 1
                            print("user:", user_answer)
                            print("score:", score)
                        break
                    else:
                        print("Input a valid option\n")

        # print(score)
        question_num += 1


def get_input(text):
    return input(f"Enter {text}: ")


if __name__ == "__main__":
    main()

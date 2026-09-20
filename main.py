from test_trivia_questions import questions
import random


# num_ten = [1,2,3,4,5,6,7,8,9,0]
def main():
    random.shuffle(questions)
    question_num = 1
    score = 0
    for question in questions:
        # question = questions[i]
        # print(f"question: {question}")
        for key, value in question.items():
            if key == "question":
                print(f'[{question_num}] {question["question"]}')
                for option in question["options"]:
                    print(option)
                get_input("your answer")
        question_num += 1


def get_input(text):
    return input(f"Enter {text}: ")


if __name__ == "__main__":
    main()

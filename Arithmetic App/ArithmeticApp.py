import random


def generate_problem():
    first = random.randint(1, 100)
    second = random.randint(1, first)
    return first, second


def calculate_answer(first, second):
    return first - second


def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def ask_question(first, second):
    correct_answer = calculate_answer(first, second)

    for attempt in range(1, 3):
        user_answer = int(input(f"{first} - {second} = "))

        if check_answer(user_answer, correct_answer):
            print("Correct!")
            return True
        else:
            print("Wrong!")

    print("Correct answer is:", correct_answer)
    return False


def run_quiz():
    score = 0

    for question_number in range(1, 11):
        print(f"\nQuestion {question_number}")

        first, second = generate_problem()

        if ask_question(first, second):
            score += 1

    print("\nFinal score:", score, "out of 10")
    return score

if __name__ == "__main__":
run_quiz()
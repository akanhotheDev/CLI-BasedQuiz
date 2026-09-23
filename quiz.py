import json
from json.decoder import JSONDecodeError
import random

allowed_options = ["a", "b", "c", "d", "end"]

def load_question():
    try:
        with open("questions.json", "r") as q:
            questions = json.load(q)
    except JSONDecodeError:
        print("Error loading questions")
        questions = []
    except FileNotFoundError:
        print("questions.json not found")
        questions = []
    return questions

questions = load_question()
random.shuffle(questions)

def quiz():
    score = 0
    counter = 0
    for ask in questions:
        counter += 1
        print(f"==> {counter}. {ask['question']} <==")
        for i in ask["options"]:
            print(f"[..{i}..]")
        choice = input().lower().strip()

        # keep asking until they give a non-empty, allowed option
        while choice == "" or choice not in allowed_options:
            if choice == "":
                print("You didn't enter anything")
            else:
                print(f'You are only allowed to choose from {allowed_options}')
            print(f"==> {counter}. {ask['question']} <==")
            for i in ask["options"]:
                print(f"[..{i}..]")
            choice = input().lower().strip()

        # now choice is guaranteed valid — evaluate it once
        if choice == "end":
            print(f"You ended the Quiz\nTotal score: {score}")
            print("="*20)
            break
        elif choice.upper() == ask["answer"]:
            print("Correct answer")
            print("="*15, "\n")
            score += 1
        else:
            print("Wrong answer")
            print(f"Your choice: {choice}\ncorrect answer: {ask['answer']}")
            print("="*20, "\n")

    print(f"Out of {counter}, you got {score} right")
    print(f"Your total score is: {score}")
    print("-"*20)

quiz()
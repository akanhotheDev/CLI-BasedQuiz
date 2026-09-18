
import random
def Quiz():
    statmessg = "Quiz Ended"
    welcmessg = "----> This is A CLI Based Quiz <----\n----> Enter 'end' to stop the quiz at anytime <----"
    print(welcmessg)
    score = 0
    choice = ""
    allowed_options = ["a","b","c","d", "end"]

    questions = [
        {
            "question": "What is the fastest land animal?", 
            "options": ["A. Cheetah", "B. Lion", "C. Goat", "JD. aguar"],
            "answer": "A".lower()
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Au", "B. CH", "C. Go", "D. Gd"],
            "answer": "A".lower()
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["A. Earth", "B. Jupiter", "C. Mercury", "D. Satus"],
            "answer": "C".lower()
        },
        {
            "question": "Who wrote the Harry Potter series?",
            "options": ["A. Whit Whatman", "B. None", "C. J.K. Rowling", "D. Bryan Thomas"],
            "answer": "C".lower()
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A. Avocado", "B. Citric", "C. Lemon", "D. Papaya"],
            "answer": "A".lower()
        },
        {
            "question": "Which ocean is the largest on Earth?",
            "options": ["A. Madagascar sea", "B. The Pacific Ocean", "C. The Atlantic Ocean", "D. River Benue"],
            "answer": "B".lower()
        },
        {
            "question": "What animal can be seen on the Porsche logo?",
            "options": ["A. Bull", "B. Horse", "C. Pheonix", "D. Cheetah"],
            "answer": "B".lower()
        },
        {
            "question": "What food never spoils",
            "options": ["A. Beans", "B. Honey", "C. Dry Rice", "D. Garri"],
            "answer": "B".lower()
        },
        {
            "question": "What is the capital of Spain?",
            "options": ["A. Madrid", "B. Porto-rico", "C. New York", "D. New Jersey"],
            "answer": "A".lower()
        },
        {
            "question": "Which planet is the largest in the Solar System?",
            "options": ["A. Earth", "B. Venus", "C. Jupiter", "D. Mars"],
            "answer": "C".lower()
        }
    ]
    random.shuffle(questions)

    for ask in questions:
        print(f"==> {ask['question']} <==")
        print(f"==> {ask['options']} <==")
        choice = input().lower()
        if len(choice) == 0:
            while choice == "":
                print("You didnt enter anything")
                choice = input()

       
        elif choice == "end":
            statmessg = "You ended the Quiz"
            print(f"Your choice: {choice}\nTotal score: {score}")
            print("="*20)
            break  
            
        elif choice == ask["answer"]:
            statmessg = "Correct answer"
            print(statmessg)
            print("="*15, "\n")
            score += 1
        elif len(choice) >= 1:
             
            while choice not in allowed_options:
                print(f'Your allowed to only choose from {allowed_options}')
                print(f"==> {ask['question']} <==")
                print(f"==> {ask['options']} <==")
                choice = input()
                if choice == ask["answer"]:
                    statmessg = "Correct answer"
                    print(statmessg)
                    print("="*20, "\n")
                    score += 1
                else:
                    statmessg = "Wrong answer"
                    print(statmessg)
                    print(f"Your choice: {choice}\ncorrect answer: {ask['answer']}")
                    print("="*20, "\n")
            if choice == ask["answer"]:
                statmessg = "Correct answer"
                print(statmessg)
                print("="*20, "\n")
                score += 1
            else:
                statmessg = "Wrong answer"
                print(statmessg)
                print(f"Your choice: {choice}\ncorrect answer: {ask['answer']}")
                print("="*20, "\n")

        else:
            statmessg = "Wrong answer"
            print(statmessg)
            print(f"Your choice: {choice}\ncorrect answer: {ask['answer']}")
            print("="*10, "\n")

    print(statmessg, "\n")
    print(f"Out of {len(questions)}, you got {score} right")
    print(f"Your total score is: {score}")
    print("-"*20)

Quiz()
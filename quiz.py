# A CLI Based Quiz

# start
# - print "Welcom mssg"
# - Score = 0
# - questions = [{"question": "", "options": [], "answer": ""]


def Quiz():
    print("This is A CLI Based Quiz")
    score = 0
    questions = [
        {
            "question": "What is the fastest land animal?", 
            "options": ["Cheetah", "Lion", "Goat", "Jaguar"],
            "answer": "cheetah".lower()
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "CH", "Go", "Gd"],
            "answer": "Au".lower()
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Earth", "Jupyter", "Mercury", "Satus"],
            "answer": "Mercury".lower()
        },
        {
            "question": "Who wrote the Harry Potter series?",
            "options": ["Whit Whatman", "None", "J.K. Rowling", "Bryan Thomas"],
            "answer": "J.K. Rowling".lower()
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Avocado", "Citric", "Lemon", "Papaya"],
            "answer": "Avocado".lower()
        },
        {
            "question": "Which ocean is the largest on Earth?",
            "options": ["Madagascar sea", "The Pacific Ocean", "The Atlantic Ocean", "River Benue"],
            "answer": "The Pacific Ocean".lower()
        },
        {
            "question": "What animal can be seen on the Porsche logo?",
            "options": ["Bull", "Horse", "Pheonix", "Cheetah"],
            "answer": "Horse".lower()
        },
        {
            "question": "What food never spoils",
            "options": ["Beans", "Honey", "Dry Rice", "Garri"],
            "answer": "Honey".lower()
        },
        {
            "question": "What is the capital of Spain?",
            "options": ["England", "Porto-rico", "New York", "New Jersey"],
            "answer": "Madrid".lower()
        },
        {
            "question": "Which planet is the largest in the Solar System?",
            "options": ["Earth", "Venus", "Jupiter", "Mars"],
            "answer": "Jupiter".lower()
        }
    ]
    for ask in questions:
        print(ask["question"])
        print(ask["options"])

Quiz()
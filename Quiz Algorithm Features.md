# Quiz Algorithm
** Features **
- Display questions
- Display multiple-choice options
- Accept user answers
- Check answers
- Keep score
- Display final results
- Randomize questions

start
    welcome message
    set score to zero
    list/ group of questions
    loop for specified times
        display question randomly from group of questions
            display multiple-choice options
            accept user answers
            verify answer
                if answer is correct display "correct" and add to score 
                esle if answer is wrong don't add to score else display "Wrong"
    end loop
    display "Quiz ended" and Final result


## Pseudo-code
start
- print "Welcom mssg"
- Score = 0
- questions = [{"question": "", "options": [], "answer": ""]
- for levels in range(5)
    print(questions[question])
    print(questions[options]\n)
    choice = input()
    if choice == questions([answer])
        print("Correct")
        score += 1
    else print("wrong")
         print(f"correct answer is: {questions([answers])
        
- end loop
- print("Quiz ended")

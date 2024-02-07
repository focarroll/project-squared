#Python Quiz Game
def quizGame():
    questions = ("What is the longest river in the world? ",
                "Who was the first person on the moon? ",
                "Who is the richest person on Earth? ",
                "What is my favorite color? ",
                "What is unique about a tuple in python? ")

    options = (("A. Nile", "B. Amazon", "C. Yangtze", "D. Congo"),
            ("A. Eugene Cerna", "B. Buzz Aldrin", "C. Alan Shepard", "D. Neil Armstrong"),
            ("A. Elon Mush", "B. William Ding", "C. Prajogo Pangestu", "D. Zhong Shanshan"),
            ("A. Yellow", "B. Green", "C. Blue", "D. Burlywood"),
            ("A. It is used to store multiple values in a single variable", "B. It is ordered", "C. It is written in round brackets", "D. It is unchangeable"))

    answers = ("A","D","D","B","C")
    guesses = []
    score = 0
    question_num = 0

    print("Welcome to my Quiz Game! ")

    for question in questions:
        print("*******************")
        print (question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A,B,C, or D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print ("CORRECT")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("***********************")
    print("QUESTIONS COMPLETED")
    print("***********************")
    print("Answers: ", end="")

    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses: ", end = "")
    for guess in guesses:
        print(guess, end = " ")
    print()

    print(f"You got {score}/" + str(len(questions)))
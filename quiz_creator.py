import json

quiz = []

while True:
    question_data = {} # saving quiz data

    # ask user for questions with choices a b c d
    question_data["question"] = input("Enter a question: ")
    question_data["a"] = input("Choice 1 (a): ")
    question_data["b"] = input("Choice 1 (b): ")
    question_data["c"] = input("Choice 1 (c): ")
    question_data["d"] = input("Choice 1 (d): ")

    # ask for the right answer or choice
    while True:
        question_data["correct_choice"] = input("Correct answer: ").lower()     # save the data
        if question_data["correct_choice"] in ["a", "b", "c", "d"]:
            quiz.append(question_data) # adding question data in the quiz list)
            break
        else:
            print("Not in choices")

    # exit until the user exits
    while True:
        another_q = input("Another question? (y/n): ").lower()
        if another_q == "y":
            break
        elif another_q == "n":
            with open("quiz.txt", "w") as file:    # saving the data in txt file
                json.dump(quiz, file, indent = 4)
            print('Quiz saved to "quiz.txt"')
            exit()
        else:
            print("Please enter y or n")
        
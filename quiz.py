import json
import random

# display quiz details
print("Instruction:\n1.) only enter characters a, b, c, d.\n2.) lowercase only.\n")
print("Instructions:\n1.) only enter characters a, b, c, d.\n2.) lowercase only.\n")

# read the quiz file 
with open("quiz.txt", "r") as file:
    quiz = json.load(file)

# initialize score to 0
score = 0
total = len(quiz)

# display a random question
random.shuffle(quiz) #using shuffle to not duplicate the questions
for questions in quiz:

    print("Question:", questions["question"])
    print("a.)", questions["a"])
    print("b.)", questions["b"])
    print("c.)", questions["c"])
    print("d.)", questions["d"])

    # ask user for their answer
    user_answer = input("Answer: ").lower().strip()

    # display the correct answer
    key = questions["correct_choice"]
    correct_answer = questions[key]
    print("Correct answer:", key)

    # if answer is correct add 1 else no score
    if user_answer == key:
        score += 1

    # display final score
    print(f"Your final score is {score}/{total}")

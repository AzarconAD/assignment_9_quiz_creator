import json

# display quiz details
print("Instruction:\n1.) only enter characters a, b, c, d.\n2.) lowercase only.\n")

# initialize score to 0
score = 0

# read the quiz file 
with open("quiz.txt", "r") as file:
    print(file.read())



# display a random question
# ask user for their answer
# display the correct answer
# if answer is correct add 1 else no score
# repeat until no question left
# display final score
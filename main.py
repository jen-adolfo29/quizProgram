# quiz
# dictionary that stores q&a
# have a variable that tracks the score of the player

quiz = {
    "q1": {
        "question": "Who killed the Night King?",
        "answer": "Arya Stark"
    },
    "q2": {
        "question": "Who was the last Lannister alive?",
        "answer": "Tyrion Lannister"
    },
    "q3": {
        "question": "How many kingdoms are there in Westeros?",
        "answer": "7"
    },
    "q4": {
        "question": "What is the name of Jon Snow’s direwolf?",
        "answer": "Ghost"
    },
    "q5": {
        "question": "How many dragons does Daenerys have?",
        "answer": "3"
    },
    "q6": {
        "question": "Who was the commander of the Unsullied?",
        "answer": "Grey Worm"
    },
    "q7": {
        "question": "Before her death, who does Olenna Tyrell admit to killing?",
        "answer": "Joffrey Lannister"
    },
    "q8": {
        "question": "What is the ancestral seat of House Lannister?",
        "answer": "Casterly Rock"
    },
    "q9": {
        "question": "What is the named of the mercenary army hired by Cersei to protect Kings Landing in Season 7?",
        "answer": "The Golden Company of Essos"
    },
    "q10": {
        "question": "What are the names of Daenerys’ dragons?",
        "answer": "Drogon, Rhaegal & Viserion"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score = score + 1
        print("Your score is: " + str(score))
    else:
        print("Wrong answer!")
        print("The correct answer is: " + value['answer'])
        print("Your score is: " + str(score))
        print("")

print("Your total score " + str(score) + "out of 10")
print("Percentage " + str(int(score/10 * 100)) + "%")
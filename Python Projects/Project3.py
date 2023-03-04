quiz = {
    "question1":{
        "question": "What's the capital of Libya?",
        "answer": "Tripoli"
    },
    "question2":{
        "question": "What's the capital of Egypt?",
        "answer": "Cairo"
    },
    "question3":{
        "question": "Who's the main charactor in One Piece?",
        "answer": "Luffy"
    },
    "question4":{
        "question": "The fair of the death is worse of the death it's self. who said that?",
        "answer": "Akai shuichi"
    },
    "question5":{
        "question": "Who beat big mam?",
        "answer": "Law and Kid"
    },
    "question6":{
        "question": "Who the best hacker in Mr.Robot?",
        "answer": "Eliot Aldroson"
    },
    "question7":{
        "question": "Segwa jotaro kesamada. who said that?",
        "answer": "Dio"
    },
    "question8":{
        "question": "What's the best charactor in Elite of Classroom?",
        "answer": "Aianakoje"
    },
}

score = 0

for key,value in quiz.items():
    print("#"*50)
    print(value["question"])
    answer = input("Enter the answer: ")
    print("#"*50)
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1
        print(f"Your score is: {score}")
        print("#"*50)
    else:
        print("Incorrect")
        print(f"Your score is: {score}")
        print("#"*50)

scorepersnatge = score/8 * 100

print(f"You final score is: {scorepersnatge}%")


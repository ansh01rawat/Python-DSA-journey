class Question:
    def __init__(self, prompt,answer):
        self.prompt = prompt
        self.answer = answer




question= [
    "what is the colour of sunrise?\n(a) red \n(b) yellow\n(c) orange \n(d) purple \n\n",
    "what is the colour of apple?\n(a)red/green \n(b) yellow \n(c) orange \n(d) purple \n\n",
    "what is the colour of strawberry?\n(a)blue \n(b)red \n(c) yellow \n(d) orange \n\n"
]
questions= [
    Question(question[0],"c"),
    Question(question[1],"a"),
    Question(question[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct answer")

run_test(questions)
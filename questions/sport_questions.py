import random
from questions.questions_class import Question
class SportQuestion(Question):
    def __init__(self):
        super().__init__()
        self.questions = [
        {
            "question": "Vilket land har vunnit flest VM-titlar i herrfotboll?",
            "options": ["a Tyskland", "b Italien", "c Brasilien", "d Argentina"],
            "answer": "c"
        },
        {
            "question": "Hur många spelare finns på plan i ett ishockeylag (per lag) under vanlig spel?",
            "options": ["a 5", " b 6", "c 7", "d 8"],
            "answer": "b"
        },
        {
            "question": "I vilken sport används termen 'love' för att beskriva noll poäng?",
            "options": ["a Badminton", "b Tennis", "c Cricket", "d Rugby"],
            "answer": "b"
        },
        {
            "question": "Vilken svensk friidrottare satte världsrekord i stavhopp 2020?",
            "options": ["a Stefan Holm", "b Armand Duplantis", "c Patrik Sjöberg", "d Kajsa Bergqvist"],
            "answer": "b"
        },
        {
            "question": "Hur lång är en maratonlöpning?",
            "options": ["a 36km", "b 40 km", "c 42km", "d 45 km"],
            "answer": "c"
        },
        {
            "question": "Vilken sport förknippas med Tiger Woods?",
            "options": ["a Golf", "b Tennis", "c Basket", "d Baseboll"],
            "answer": "a"
        },
        {
            "question": "I vilken sport kan man vinna Stanley Cup?",
            "options": ["a Fotboll", "b Ishockey", "c Baseboll", "d Basket"],
            "answer": "b"
        },
        {
            "question": "Vilket land arrangerade de Olympiska sommarspelen 2012?",
            "options": ["a Kina", "b Brasilien", "c Storbritannien", "d Grekland"],
            "answer": "c"
        },
        {
            "question": "Vad heter den kända svenska skidåkaren som vann tre OS-guld i Turin 2006?",
            "options": ["a Charlotte Kalla", "b Anja Pärson", "c Gunde Svan", "d Thomas Wassberg"],
            "answer": "b"
        },
        {
            "question": "Hur många minuter spelas en vanlig fotbollsmatch (exklusive tilläggstid)?",
            "options": ["a 60 minuter", "b 70 minuter", "c 80 minuter", "d 90 minuter"],
            "answer": "d"
        }
    ]
    '''
    def random_question(self):
        q = random.choice(self.SportQuestion)
        print(f"\nSlumpad fråga: {q['question']}")
        for option in q["options"]:
            print(option)
        return q["answer"] 
    '''
    def print_all(self):
        for i, q in enumerate(self.SportQuestion, start=1):
            print(f"\nFråga {i}: {q['question']}")
            for option in q["options"]:
                print(option)
            print(f"Rätt svar: {q['answer']}")
'''
q = SportQuestion()
q.print_all
correct_answer = q.random_question()
print(f"(Rätt svar är: {correct_answer})")
score = 0
while True:
    correct_answer = q.random_question()
    
    
    user_input = input("Ditt svar (a, b, c, d) eller 'q' för att sluta: ").lower().strip()
    
    if user_input == "q":
        print(f"\nSpelet avslutas. Du fick {score} poäng!")
        break
    
    
    if user_input == correct_answer:
        print(" Rätt!")
        score += 1
    else:
     print(f" Fel! Rätt svar är: {correct_answer}")
    
    print(f"Din poäng: {score}")
'''
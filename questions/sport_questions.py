import random
from questions.questions_class import Question
class SportQuestion(Question):
    def __init__(self):
        super().__init__()
        self.questions = [
        {
            "question": "Vilket land har vunnit flest VM-titlar i herrfotboll?",
            "options": ["A Tyskland", "B Italien", "C Brasilien", "D Argentina"],
            "answer": "C"
        },
        {
            "question": "Hur många spelare finns på plan i ett ishockeylag (per lag) under vanlig spel?",
            "options": ["A 5", " B 6", "C 7", "D 8"],
            "answer": "B"
        },
        {
            "question": "I vilken sport används termen 'love' för att beskriva noll poäng?",
            "options": ["A Badminton", "B Tennis", "C Cricket", "D Rugby"],
            "answer": "B"
        },
        {
            "question": "Vilken svensk friidrottare satte världsrekord i stavhopp 2020?",
            "options": ["A Stefan Holm", "B Armand Duplantis", "C Patrik Sjöberg", "D Kajsa Bergqvist"],
            "answer": "B"
        },
        {
            "question": "Hur lång är en maratonlöpning?",
            "options": ["A 36km", "B 40 km", "C 42km", "D 45 km"],
            "answer": "C"
        },
        {
            "question": "Vilken sport förknippas med Tiger Woods?",
            "options": ["A Golf", "B Tennis", "C Basket", "D Baseboll"],
            "answer": "A"
        },
        {
            "question": "I vilken sport kan man vinna Stanley Cup?",
            "options": ["A Fotboll", "B Ishockey", "C Baseboll", "D Basket"],
            "answer": "B"
        },
        {
            "question": "Vilket land arrangerade de Olympiska sommarspelen 2012?",
            "options": ["A Kina", "B Brasilien", "C Storbritannien", "D Grekland"],
            "answer": "C"
        },
        {
            "question": "Vad heter den kända svenska skidåkaren som vann tre OS-guld i Turin 2006?",
            "options": ["A Charlotte Kalla", "B Anja Pärson", "C Gunde Svan", "D Thomas Wassberg"],
            "answer": "B"
        },
        {
            "question": "Hur många minuter spelas en vanlig fotbollsmatch (exklusive tilläggstid)?",
            "options": ["A 60 minuter", "B 70 minuter", "C 80 minuter", "D 90 minuter"],
            "answer": "D"
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
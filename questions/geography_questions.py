import random
import datetime
import matplotlib.pyplot as plt  # Externt bibliotek
from questions.questions_class import Question

class GeographyQuiz(Question):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.questions = [
    {
        "question": "Vilket är världens största land till ytan?",
        "options": ["A) Kanada", "B) USA", "C) Ryssland", "D) Kina"],
        "answer": "C) Ryssland"
    },
    {
        "question": "Vilken är världens längsta flod?",
        "options": ["A) Nilen", "B) Amazonfloden", "C) Yangtze", "D) Mississippi"],
        "answer": "A) Nilen"
    },
    {
        "question": "Vilket land har störst befolkning i världen?",
        "options": ["A) Indien", "B) USA", "C) Kina", "D) Indonesien"],
        "answer": "A) Indien"
    },
    {
        "question": "Vad heter Kanadas huvudstad?",
        "options": ["A) Toronto", "B) Ottawa", "C) Vancouver", "D) Montreal"],
        "answer": "B) Ottawa"
    },
    {
        "question": "På vilken kontinent ligger Saharaöknen?",
        "options": ["A) Asien", "B) Afrika", "C) Australien", "D) Sydamerika"],
        "answer": "B) Afrika"
    },
    {
        "question": "Vilket land består av flest öar?",
        "options": ["A) Indonesien", "B) Filippinerna", "C) Japan", "D) Sverige"],
        "answer": "D) Sverige"
    },
    {
        "question": "Vilket hav ligger öster om Afrika?",
        "options": ["A) Atlanten", "B) Indiska oceanen", "C) Stilla havet", "D) Medelhavet"],
        "answer": "B) Indiska oceanen"
    },
    {
        "question": "Vilket är Europas högsta berg?",
        "options": ["A) Mont Blanc", "B) Matterhorn", "C) Elbrus", "D) Kebnekaise"],
        "answer": "C) Elbrus"
    },
    {
        "question": "I vilket land ligger pyramiderna i Giza?",
        "options": ["A) Mexiko", "B) Egypten", "C) Sudan", "D) Jordanien"],
        "answer": "B) Egypten"
    },
    {
        "question": "Vilken är världens största ö?",
        "options": ["A) Grönland", "B) Nya Guinea", "C) Borneo", "D) Madagaskar"],
        "answer": "A) Grönland"
    }]


    def start_quiz(self):
        print("\n Welcome to the Geography Quiz!\n")
        start_time = datetime.datetime.now()
        random.shuffle(self.questions)

        for q in self.questions:
            print(q["question"])
            for i, opt in enumerate(q["options"], 1):
                print(f"{i}. {opt}")

            answer = input

            if answer.isdigit() and 1 <= int(answer) <= len(q["options"]):
                chosen = q["options"][int(answer) - 1]
                if chosen == q["correct_answer"]:
                    print(" Correct!\n")
                    self.score += 1
                else:
                    print(f" Wrong! The correct answer is {q['correct_answer']}.\n")
            else:
                print(" Invalid input.\n")

        end_time = datetime.datetime.now()
        elapsed = (end_time - start_time).seconds
        print(f"You scored {self.score}/{len(self.questions)} points in {elapsed} seconds!")

        self.show_results_chart()

    def show_results_chart(self):
        labels = ['Correct', 'Incorrect']
        values = [self.score, len(self.questions) - self.score]
        plt.bar(labels, values, color=['green','red'])
        plt.title("Geography Quiz Results")
        plt.ylabel("Number of Questions")
        plt.show()


if __name__ == "__main__":
    quiz = GeographyQuiz()
    quiz.start_quiz()
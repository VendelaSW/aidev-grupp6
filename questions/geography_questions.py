import random
import datetime
import matplotlib.pyplot as plt  # Externt bibliotek

class GeographyQuiz:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "Which is the largest country in the world by area?",
                "options": ["A) Canada", "B) USA", "C) Russia", "D) China"],
                "answer": "C) Russia"
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["A) Nile", "B) Amazon River", "C) Yangtze", "D) Mississippi"],
                "answer": "A) Nile"
            },
            {
                "question": "Which country has the largest population in the world?",
                "options": ["A) India", "B) USA", "C) China", "D) Indonesia"],
                "answer": "A) India"
            },
            {
                "question": "What is the capital city of Canada?",
                "options": ["A) Toronto", "B) Ottawa", "C) Vancouver", "D) Montreal"],
                "answer": "B) Ottawa"
            },
            {
                "question": "On which continent is the Sahara Desert located?",
                "options": ["A) Asia", "B) Africa", "C) Australia", "D) South America"],
                "answer": "B) Africa"
            },
            {
                "question": "Which country consists of the most islands?",
                "options": ["A) Indonesia", "B) Philippines", "C) Japan", "D) Sweden"],
                "answer": "D) Sweden"
            },
            {
                "question": "Which ocean lies east of Africa?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Mediterranean Sea"],
                "answer": "B) Indian Ocean"
            },
            {
                "question": "What is the highest mountain in Europe?",
                "options": ["A) Mont Blanc", "B) Matterhorn", "C) Elbrus", "D) Kebnekaise"],
                "answer": "C) Elbrus"
            },
            {
                "question": "In which country are the Pyramids of Giza located?",
                "options": ["A) Mexico", "B) Egypt", "C) Sudan", "D) Jordan"],
                "answer": "B) Egypt"
            },
            {
                "question": "What is the largest island in the world?",
                "options": ["A) Greenland", "B) New Guinea", "C) Borneo", "D) Madagascar"],
                "answer": "A) Greenland"
            }
        ]

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
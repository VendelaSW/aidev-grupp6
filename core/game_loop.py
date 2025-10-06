from frågor.musik_frågor import musikfrågor

class GameLoop:
    def __init__(self):
        self.categories = [musikfrågor()]
        self.score = 0

    def start_round(self):
        print("Ny runda!\n")
        for category in self.categories:
            q = category.get_random_question()
            print(q["question"])
            print(q["options"])
            answer = input("Svar: ")
            if answer.lower() in q["answer"].lower():
                print("Rätt svar!\n")
                self.score += 1
            else:
                print(f"Fel svar! Rätt svar var {q['answer']}")
        print(f"Ditt resultat: {self.score}/{len(self.categories)}")

if __name__ == "__main__":
    game = GameLoop()
    while True:
        game.start_round()
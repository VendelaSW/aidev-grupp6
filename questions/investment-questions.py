import random  # Para generar aleatoriedad

class InvestmentQuiz:
    def __init__(self):
        # Preguntas divididas por categoría
        self.categories = {
            "Sverige": [
                ("Vilket svenskt företag är känt för sin musikstreamingtjänst?", "spotify"),
                ("Vilket svenskt företag fokuserar på telekommunikation och 5G?", "ericsson"),
                ("Vilket svenskt bilföretag ägs delvis av kinesiska Geely?", "volvo")
            ],
            "Europa": [
                ("Vilket tyskt företag äger Audi och Porsche?", "volkswagen"),
                ("Vilket nederländskt företag är världsledande på chipstillverkning?", "asml"),
                ("Vilket franskt företag äger Louis Vuitton och Dior?", "lvmh")
            ],
            "Internationellt": [
                ("Vilket amerikanskt företag äger YouTube?", "google"),
                ("Vilket amerikanskt företag är störst på elbilar?", "tesla"),
                ("Vilket kinesiskt företag äger e-handelsplattformen Alibaba?", "alibaba"),
                ("Vilket amerikanskt företag grundades av Jeff Bezos?", "amazon")
            ]
        }

    # Función que ejecuta el quiz según categoría
    def start_quiz(self):
        print("Välj kategori:")
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")

        choice = int(input("Skriv numret på kategorin du vill spela: "))
        category_name = list(self.categories.keys())[choice - 1]

        questions = self.categories[category_name]
        random.shuffle(questions)

        score = 0
        for question, correct_answer in questions:
            answer = input(question + " ").lower()
            if answer == correct_answer:
                print("Rätt! ✅")
                score += 1
            else:
                print(f"Fel! ❌ Rätt svar är: {correct_answer}")

        print(f"\nDu fick {score} av {len(questions)} poäng i kategorin {category_name}!")

    # Función para permitir jugar varias veces
    def play(self):
        print("💸 Välkommen till Investerings-Quizet! 💸")
        print("Är du redo att visa vad du kan om världens största företag?")
        
        ready = input("Svara 'ja' för att börja eller 'nej' för att avsluta: ").lower()
        if ready != "ja":
            print("Okej, kanske nästa gång! 👋")
            return  # Sale de la función si el jugador no quiere jugar

        print("\nToppen! Då kör vi igång!\n")
        
        while True:
            self.start_quiz()
            again = input("Vill du spela igen? (ja/nej): ").lower()
            if again != "ja":
                print("Tack för att du spelade! 👋")
                break


if __name__ == "__main__":
    quiz = InvestmentQuiz()
    quiz.play()
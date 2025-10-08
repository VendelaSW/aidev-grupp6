import random  # Para mezclar o elegir preguntas al azar


class InvestmentQuestions:
    def __init__(self):
        self.questions = [
            {
                "question": "Vilket svenskt företag är känt för sin musikstreamingtjänst och har investerat i AI-ljudteknik?",
                "options": ["A) Klarna", "B) Spotify", "C) Volvo", "D) Ericsson"],
                "answer": "B) Spotify"
            },
            {
                "question": "Vilket svenskt företag investerar i 5G-nätverk och telekomlösningar?",
                "options": ["A) IKEA", "B) Volvo", "C) Ericsson", "D) Sandvik"],
                "answer": "C) Ericsson"
            },
            {
                "question": "Vilket svenskt bilföretag ägs delvis av kinesiska Geely?",
                "options": ["A) Saab", "B) Scania", "C) Polestar", "D) Volvo"],
                "answer": "D) Volvo"
            },
            {
                "question": "Vilket tyskt företag äger bilmärkena Audi och Porsche?",
                "options": ["A) Mercedes", "B) Volkswagen", "C) BMW", "D) Opel"],
                "answer": "B) Volkswagen"
            },
            {
                "question": "Vilket nederländskt företag är världsledande inom chipstillverkning?",
                "options": ["A) ASML", "B) Philips", "C) Shell", "D) Unilever"],
                "answer": "A) ASML"
            },
            {
                "question": "Vilket franskt företag äger Louis Vuitton och Dior?",
                "options": ["A) Chanel", "B) Hermès", "C) LVMH", "D) Cartier"],
                "answer": "C) LVMH"
            },
            {
                "question": "Vilket amerikanskt företag äger YouTube?",
                "options": ["A) Meta", "B) Google", "C) Microsoft", "D) Netflix"],
                "answer": "B) Google"
            },
            {
                "question": "Vilket amerikanskt företag är världens största elbilstillverkare?",
                "options": ["A) Ford", "B) Tesla", "C) Rivian", "D) Lucid Motors"],
                "answer": "B) Tesla"
            },
            {
                "question": "Vilket kinesiskt företag äger e-handelsplattformen Alibaba?",
                "options": ["A) Tencent", "B) JD.com", "C) Baidu", "D) Alibaba"],
                "answer": "D) Alibaba"
            },
            {
                "question": "Vilket amerikanskt företag grundades av Jeff Bezos 1994?",
                "options": ["A) eBay", "B) Amazon", "C) PayPal", "D) Microsoft"],
                "answer": "B) Amazon"
            }
        ]

    # Función simple para jugar el quiz
    def play(self):
        print("💸 Välkommen till Investerings-Quizet! 💸")
        print("Är du redo att visa vad du kan om världens största företag?")
        
        ready = input("Svara 'ja' för att börja eller 'nej' för att avsluta: ").lower()
        if ready != "ja":
            print("Okej, kanske nästa gång! 👋")
            return

        print("\nToppen! Då kör vi igång!\n")
        random.shuffle(self.questions)
        score = 0

        for q in self.questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)

            answer = input("Skriv ditt svar (t.ex. A, B, C eller D): ").upper()
            if answer in q["answer"]:
                print("Rätt! ✅")
                score += 1
            else:
                print(f"Fel! ❌ Rätt svar är: {q['answer']}")

        print(f"\nDu fick {score} av {len(self.questions)} poäng! 👏")

if __name__ == "__main__":
    quiz = InvestmentQuestions()
    quiz.play()
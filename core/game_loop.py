from questions.music_questions import MusicQuestions
from questions.geography_questions import GeographyQuiz
from questions.psychology_questions import Psychology
from questions.sport_questions import SportQuestion
from questions.investment_questions import InvestmentQuestions
import random

class GameLoop:
    def __init__(self):
        self.categories = [MusicQuestions(), GeographyQuiz(), Psychology(), SportQuestion(), InvestmentQuestions()]
        self.score = 0

    import random

    def get_question_from_category(self, category):
        """
        Safely get a question from a category class.
        Handles missing methods, messy print logic, and direct lists.
        """
        # 1️⃣ If the category has a proper method
        if hasattr(category, "get_random_question") and callable(category.get_random_question):
            try:
                return category.get_random_question()
            except:
                pass
        '''
        # 2️⃣ Special hack for SportQuestion
        if isinstance(category, SportQuestion):
            # Call random_question, but build a dict manually
            q_index = random.randint(0, len(category.SportQuestion)-1)
            q = category.SportQuestion[q_index]
            return {
                "question": q["question"],
                "options": q["options"],
                "answer": q["answer"]
            }
        '''
        # 3️⃣ Fallback for other lists
        for attr_name in ["questions", "frågor", "quiz", "data"]:
            if hasattr(category, attr_name):
                questions = getattr(category, attr_name)
                if isinstance(questions, list) and questions:
                    return random.choice(questions)

        return {"question": "No question found", "options": [], "answer": None}


    def start_round(self):
        print("Ny runda!\n")
        for category in self.categories:
            q = self.get_question_from_category(category)
            if not q or "question" not in q:
                continue
            # after selecting a question dict
            if "answer" not in q and "correct_answer" in q:
                q["answer"] = q["correct_answer"]

            print(q["question"])
            if q.get("options"):
                for option in q["options"]:
                    print(option)
            else:
                print("[Inga alternativ tillgängliga]")
            
            answer = input("Svar: ")
            if q.get("answer") and answer.lower().strip() in q["answer"].lower().strip():
                print("Rätt svar!\n")
                self.score += 1
            else:
                print(f"Fel svar! Rätt svar var {q.get('answer', 'okänt')}\n")

        print(f"Ditt resultat: {self.score}/{len(self.categories)}")

if __name__ == "__main__":
    game = GameLoop()
    while True:
        game.start_round()
import random

class Psychology:
    def __init__(self):
        self.score = 0
        self.total_questions = 0

        # En variabel som håller både frågorna, alternativen och svaren i en dictionary lista
        self.questions = [
            {
                "question": "Hur menade Piaget att moral utvecklas hos barn?",
                "options": [
                    "A) Genom imitering av vuxnas beteenden",
                    "B) Genom genetiska faktorer",
                    "C) Genom religiös undervisning",
                    "D) Genom interaktion och samspel med andra så som lek"
                ],
                "answer": "D"
            },
            {
                "question": "När man försöker sluta med missbruk av alkohol eller porr är ett vanligt abstinenssymptom att man känner vadå?",
                "options": [
                    "A) Sötsug",
                    "B) Rastlöshet",
                    "C) Huvudvärk",
                    "D) Ångest"
                ],
                "answer": "D"
            },
            {
                "question": "Vilken behandling har bäst bevisat stöd mot oro och ältande tankar?",
                "options": [
                    "A) Samtalsterapi",
                    "B) KBT",
                    "C) Hypnos",
                    "D) Psykedeliska droger"
                ],
                "answer": "B"
            },
            {
                "question": "Varför aktiveras amygdalan vid en muntlig presentation inför andra?",
                "options": [
                    "A) Den tolkar situationen som ett hot",
                    "B) Den styr aptiten och gör en hungrig",
                    "C) Den triggar nostalgiska minnen",
                    "D) Den aktiverar kreativt tänkande"
                ],
                "answer": "A"
            },
            {
                "question": "Vilka delar av människan menade Freud att samhället förtrycker?",
                "options": [
                    "A) Hungerkänslor",
                    "B) Självbilder",
                    "C) Sexualitet och aggressivitet",
                    "D) Drömmar"
                ],
                "answer": "C"
            },
            {
                "question": "Varför är slotmaskiner särskilt beroendeframkallande?",
                "options": [
                    "A) Las Vegas har funnits i över 100 år",
                    "B) De använder högre insatser än andra spel",
                    "C) När man trycker på knappen frigörs automatiskt dopamin",
                    "D) Maskinen ger belöningar utifrån slumpmässiga intervaller"
                ],
                "answer": "D"
            },
            {
                "question": "Vad beskriver begreppet kognitiv dissonans?",
                "options": [
                    "A) Konflikt mellan tankar och handlingar",
                    "B) Att inte kunna tolka sensorisk information",
                    "C) Att glömma minnen efter trauma",
                    "D) Konflikt mellan olika känslor samtidigt"
                ],
                "answer": "A"
            },
            {
                "question": "Vilken strategi fungerar bäst enligt inlärningspsykologi för att få barn att upprätthålla städning av sitt rum?",
                "options": [
                    "A) Belöna med veckopeng när de städar",
                    "B) Bestraffa med utegångsförbud om de inte städar",
                    "C) Att då och då ge uppskattning för att barnet städade",
                    "D) Städa rummet själv och hoppas barnet hjälper"
                ],
                "answer": "C"
            },
            {
                "question": "I vilket land växer många barn upp med undvikande anknytningsstrategi?",
                "options": [
                    "A) Japan",
                    "B) Israel",
                    "C) Tyskland",
                    "D) USA"
                ],
                "answer": "C"
            },
            {
                "question": "Vem populariserade psykologiska försvarsmekanismer som projicering och bortträngning?",
                "options": [
                    "A) Anna Freud",
                    "B) Astrid Lindgren",
                    "C) Jonas Gardell",
                    "D) Carl Rogers"
                ],
                "answer": "A"
            }
        ]

        # Separat lista med ledtrådar (matchar index)
        self.hints = [
            "Vad gör barn helst?",
            "Känsligt obehag – inte fysiskt",
            "Den mest evidensbaserade terapimetoden",
            "Stresspåslag",
            "Handlar om de mest grundläggande mänskliga drifterna…",
            "Fundera på vad som händer när belöningar kommer oregelbundet.",
            "Vad är det som inte stämmer överens?",
            "Hur skulle du själv velat bli bemött?",
            "Ett land känt för ansvar och självständighet",
            "Barnet till…"
        ]

    def ask_random_question(self):
        index = random.randint(0, len(self.questions) - 1)
        fråga = self.questions[index]

        print("\n🧠", fråga["question"])
        for option in fråga["options"]:
            print(option)

        user_input = input("Skriv ditt svar (A-D), eller 'ledtråd' för tips: ").upper()

        if user_input == "LEDTRÅD":
            print("💡 Ledtråd:", self.hints[index])
            user_input = input("Skriv ditt svar (A-D): ").upper()

        if user_input == fråga["answer"]:
            print("✅ Rätt svar!")
            self.score += 1
        else:
            print(f"❌ Fel svar. Rätt svar var {fråga['answer']}.")

# Testkörning
if __name__ == "__main__":
    quiz = Psychology()
    quiz.ask_random_question()
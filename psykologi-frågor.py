# PSEUDOKOD för mig själv
# Behöver någonstans att lagra frågorna i - Typ en class och en lista - Psykologi class och en lista med frågorna
# Behöver kunna hålla koll på poängen - Typ genom en variabel self.score
# Behöver kunna slumpa vilken ordning frågorna kommer - Typ en funktion

# import från pythons egna bibliotek för att kunna slumpa frågorna senare
import random

# Har skapat en class och 2 variabler för att komma igång.
class Psychology:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        
        # Gjorde en lista för alla frågor
        self.questions = [
            "Vilka delar av människan menade Freud att samhället förtrycker?",
            "När man försöker sluta med missbruk av alkohol eller porr är ett vanligt abstinenssymptom att man känner vadå?",
            "Varför är slotmaskiner särskilt beroendeframkallande?",
            "Vad beskriver begreppet kognitiv dissonans?",
            "Vilken strategi fungerar bäst enligt inlärningspsykologi för att få barn att upprätthålla städning av sitt rum?",
            "Varför aktiveras amygdalan vid en muntlig presentation inför andra?",
            "Hur menade Piaget att moral utvecklas hos barn?",
            "I vilket land växer många barn upp med undvikande anknytnings strategi?",
            "Vem populariserade psykologiska försvarsmekanismer som projicering och bortträngning?",
            "Vilken behandling har bäst bevisat stöd mot oro och ältande tankar?"
        ]

        # Och en separat lista för alla svarsalternativ
        self.options = [
            # Freud – inre konflikt
            ["Hungerkänslor", "Självbilder", "Sexualitet och aggressivitet", "Drömmar"],
            # Alkohol och Porr beroende
            ["Sötsug", "Rastlöshet", "Huvudvärk", "Ångest"],
            # Slotmaskiner – beroende
            ["Las Vegas har funnits i över 100 år", "De använder högre insatser än andra spel", 
             "När man trycker på knappen frigörs automatiskt dopamin", "Maskinen ger belöningar utifrån slumpmässiga intervaller"],
            # Kognitiv dissonans
            ["Konflikt mellan tankar och handlingar", "Att inte kunna tolka sensorisk information", 
             "Att glömma minnen efter trauma", "Konflikt mellan olika känslor samtidigt"],
            # Inlärningspsykologi – barns städvanor
            ["Belöna med veckopeng när de städar", "Bestraffa med utegångsförbud om de inte städar", 
             "Att då och då ge uppskattning för att barnet städade", "Städa rummet själv och hoppas barnet hjälper"],
            # Amygdalan – stress
            ["Den tolkar situationen som ett hot", "Den styr aptiten och gör en hungrig", 
             "Den triggar nostalgiska minnen", "Den aktiverar kreativt tänkande"],
            # Utvecklingspsykologi – moral
            ["Genom imitering av vuxnas beteenden", "Genom genetiska faktorer", 
             "Genom religiös undervisning", "Genom interaktion och samspel med andra så som lek"],
            # Anknytningsteori
            ["Japan", "Israel", "Tyskland", "USA"],
            # Anna Freud – försvarsmekanismer
            ["Anna Freud", "Astrid Lindgren", "Jonas Gardell", "Carl Rogers"],
            # Ältande tankar
            ["Samtalsterapi", "KBT", "Hypnos", "Psykadeliska droger"]
        ]
 
        # Och sen en tredje lista med de rätta svaren utifrån deras index position i listan
        self.answers = [
            2,  # Freud: Sexualitet och aggressivitet
            3,  # Alkohol/porr: Ångest
            3,  # Slotmaskiner: Slumpmässiga intervaller
            0,  # Kognitiv dissonans: Konflikt mellan tankar och handlingar
            2,  # Städvanor: Ge uppskattning ibland
            0,  # Amygdala: Hot
            3,  # Piaget: Samspel/lek
            2,  # Anknytning: Tyskland
            0,  # Försvarsmekanismer: Anna Freud
            1   # Ältande: KBT
        ]

        # Ledtrådar
        self.hints = [
            "Handlar om de mest grundläggande mänskliga…",
            "Känsligt obehag inte fysiskt",
            "Fundera på vad som händer när belöningar kommer oregelbundet.",
            "Vad är det som inte stämmer överens?",
            "Hur skulle du själv velat bli bemött?",
            "Stresspåslag",
            "Vad gör barn helst?",
            "Ett land känt för ansvar och självständighet",
            "Barnet till…",
            "Den mest evidensbaserad terapimetoden"
        ]

    # Slumpar fram ett index mellan 0 och antalet frågor - 1 så att jag kan hämta en slumpmässig fråga ur listan
    def get_random_index(self):
        return random.randint(0, len(self.questions) - 1)

    # Behöver en funktion för att ställa en fråga som går att återanvända flera gånger
    def ask_question(self, index):
        print("\n" + self.questions[index])

        # För att kunna visa alternativen till frågan med en sifferkoppling
        for i, option in enumerate(self.options[index]):
            print(f"{i}: {option}")

        # För att användaren ska kunna skriva in ett svar eller be om ledtråd
        user_input = input("Skriv ditt svar (0-3), eller 'ledtråd' för tips: ")

        # Vill att användaren ska kunna skriva nytt svar efter att ha fått ledtråd och att det inte blir problem med bokstäverna
        if user_input.lower() == "ledtråd":   # Användaren ber om ledtråd
            print("💡 Ledtråd:", self.hints[index])
            user_input = input("Skriv ditt svar (0-3): ")

        # Vill inte att koden crashar om någon skriver in en bokstav istället för siffra
        if user_input.isdigit():
            answer = int(user_input)

            # För att hålla koll på antal frågor
            self.total_questions += 1

            # Behöver kunna kolla om användarens siffra matchar rätt svar
            if answer == self.answers[index]:
                print("✅ Rätt svar!")
                self.score += 1
            else:
                print("❌ Fel svar.")
        else:
            print("⚠️ Ogiltig input – ingen poäng.")

# För att kunna testa min kod själv utan att det blir problem när psykolog-frågor.py filen importeras till main.py
if __name__ == "__main__":
    quiz = Psychology()
    index = quiz.get_random_index()
    quiz.ask_question(index)


# Behöver sen lägga till variables med olika datatypes
# Behöver även functions/methods - Hur sätter jag upp dessa?
# Behöver även nån form av conditions (if(elif/else) och ev loop


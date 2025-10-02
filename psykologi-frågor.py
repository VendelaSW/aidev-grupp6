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

    # Slumpar fram ett index mellan 0 och antalet frågor - 1 så att jag kan hämta en slumpmässig fråga ur listan
    def get_random_index(self):
        return random.randint(0, len(self.questions) - 1)

# För att testa om koden fungerar så la jag till ett objekt och print
if __name__ == "__main__":
    quiz = Psychology()
    index = quiz.get_random_index()
    print("Fråga:", quiz.questions[index])
    print("Alternativ:", quiz.options[index])
    print("Rätt svar är index:", quiz.answers[index])

# Behöver sen lägga till variables med olika datatypes
# Behöver även functions/methods - Hur sätter jag upp dessa?
# Behöver även nån form av conditions (if(elif/else) och ev loop


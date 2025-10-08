import json
import os


class Scoreboard:
    def __init__(self, filename="results.json"):
        self.filename = filename  # Spara filnamnet
        # Om filen inte redan finns, skapa en ny tom JSON-fil
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def save_score(self, name, score, total, time):
        """Spara ett nytt resultat i JSON-filen"""
        new_result = {
            "name": name,
            "score": score,
            "total": total,
            "time": time
        }

        # Läs in befintliga resultat
        with open(self.filename, "r") as f:
            data = json.load(f)

        # Lägg till det nya resultatet i listan
        data.append(new_result)

        # Skriv tillbaka allt till filen
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def show_top_scores(self):
        """Visa de senaste 5 resultaten"""
        with open(self.filename, "r") as f:
            data = json.load(f)

        # Om inga resultat finns, visa ett meddelande och avsluta funktionen
        if not data:
            print("No scores saved yet!\n")
            return

        # Annars skriv ut scoreboarden
        print("\nSCOREBOARD")
        for entry in data[-5:]:  # Visa de senaste 5 resultaten
            print(f"{entry['name']} - {entry['score']}/{entry['total']} points in {entry['time']}s")
            
if __name__ == "__main__":
    scoreboard = Scoreboard()  # Skapar eller laddar "results.json"

    # Lägg till några testresultat
    scoreboard.save_score("Alice", 8, 10, 25)
    scoreboard.save_score("Bob", 6, 10, 32)
    scoreboard.save_score("Charlie", 10, 10, 20)

    # Visa topplistan
    scoreboard.show_top_scores()

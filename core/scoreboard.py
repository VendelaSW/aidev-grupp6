import json
import os
from core.login import Account

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/results_data.json')
class Scoreboard:
    def __init__(self, filename=DATA_FILE):
        self.filename = filename  # Spara filnamnet
        # Om filen inte redan finns, skapa en ny tom JSON-fil
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def save_score(self, account, score, total, time):
        """Spara ett nytt resultat i JSON-filen"""
        if not account.is_logged_in():
            print("Ingen användare är inloggad, kan inte spara resultat.")
            return
        
        name = account.logged_in_user
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

    def show_top_scores(self, limit=5):
        with open(self.filename, "r") as f:
            data = json.load(f)

        if not data:
            print("No scores saved yet!\n")
            return

        # Sort by score descending, then by time ascending
        top_scores = sorted(data, key=lambda x: (-x['score'], x['time']))

        print("\n--- SCOREBOARD ---")
        for entry in top_scores[:limit]:
            print(f"""{entry['name']} - {entry['score']}/
                  {entry['total']} points in {entry['time']}s""")


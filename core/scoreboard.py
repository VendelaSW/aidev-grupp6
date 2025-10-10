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

        # Aggregate results by player
        aggregated = {}
        for entry in data:
            name = entry["name"]
            score = entry["score"]
            total = entry["total"]
            time = entry.get("time", 0)  # some older entries might not have time
            if name not in aggregated:
                aggregated[name] = {"points": 0, "attempts": 0, "time": 0}
            aggregated[name]["points"] += score
            aggregated[name]["attempts"] += total
            aggregated[name]["time"] += time

        # Calculate accuracy for each player
        results = []
        for name, stats in aggregated.items():
            points = stats["points"]
            attempts = stats["attempts"]
            total_time = stats["time"]
            accuracy = (points / attempts) * 100 if attempts > 0 else 0
            results.append({
                "name": name,
                "points": points,
                "attempts": attempts,
                "accuracy": accuracy,
                "time": total_time
            })

        # Sort by accuracy descending, then by time ascending
        top_scores = sorted(results, key=lambda x: (-x["accuracy"], x["time"]))

        print("\n--- SCOREBOARD ---")
        for entry in top_scores[:limit]:
            print(f"{entry['name']}: {entry['points']}/{entry['attempts']} "
                f"({entry['accuracy']:.1f}% korrekt) in {entry['time']}s")
        print("-------------------\n")




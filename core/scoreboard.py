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

        # Track best round per player
        best_rounds = {}
        for entry in data:
            name = entry["name"]
            score = entry["score"]
            total = entry["total"]
            time = entry.get("time", 0)
            accuracy = (score / total) * 100 if total > 0 else 0

            if name not in best_rounds:
                best_rounds[name] = {"score": score, "total": total, "accuracy": accuracy, "time": time}
            else:
                # Replace only if this round is better by accuracy, or equal accuracy but faster
                current_best = best_rounds[name]
                if accuracy > current_best["accuracy"] or (accuracy == current_best["accuracy"] and time < current_best["time"]):
                    best_rounds[name] = {"score": score, "total": total, "accuracy": accuracy, "time": time}

        # Convert to list and sort by accuracy descending, then time ascending
        top_scores = sorted(best_rounds.items(),
                            key=lambda x: (-x[1]["accuracy"], x[1]["time"]))

        print("\n--- SCOREBOARD ---")
        for name, stats in top_scores[:limit]:
            print(f"{name}: {stats['score']}/{stats['total']} "
                f"({stats['accuracy']:.1f}% korrekt) in {stats['time']}s")
        print("-------------------\n")

    def get_top_scores(self, limit=5):
        with open(self.filename, "r") as f:
            data = json.load(f)

        if not data:
            return []

        best_rounds = {}
        for entry in data:
            name = entry["name"]
            score = entry["score"]
            total = entry["total"]
            time = entry.get("time", 0)
            accuracy = (score / total) * 100 if total > 0 else 0

            if name not in best_rounds or accuracy > best_rounds[name]["accuracy"] or \
            (accuracy == best_rounds[name]["accuracy"] and time < best_rounds[name]["time"]):
                best_rounds[name] = {"name": name, "score": score, "total": total, "accuracy": accuracy, "time": time}

        # Return list of dicts including the name
        top_scores = sorted(best_rounds.values(), key=lambda x: (-x["accuracy"], x["time"]))
        return top_scores[:limit]






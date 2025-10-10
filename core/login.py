import json
import getpass
import hashlib
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/user_data.json')
class Account:
    def __init__(self):
        self.profiles = self.load_profiles()
        self.logged_in_user = None
        
    def load_profiles(self):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"profiles": {}}

    def save_profiles(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.profiles, file, indent=4)

    def create_profile(self):
        name = input("Ange ett namn för profilen: ").strip()

        if not name:
            print("Användarnamn kan inte vara tomt.")
            return None


        if name in self.profiles["profiles"]:
            print("Profilen finns redan! Vill du logga in istället?")
            if input("(ja/nej): ").strip().lower() == "ja":
                return self.login()
            return None

        while True:
            password = getpass.getpass("Ange ett lösenord: ").strip()
            if not password:
                print("Lösenord kan inte vara tomt.")
                continue
            confirm = getpass.getpass("Bekräfta lösenordet: ").strip()
            if password == confirm:
                break
            print("Lösenorden matchar inte, försök igen.")

        self.profiles["profiles"][name] = {
            "password": hashlib.sha256(password.encode()).hexdigest(),
            "points": 0,
            "attempts": 0
        }

        self.save_profiles()
        print(f"Profil för {name} skapades!\n")
        return name


    def login(self):
        if not self.profiles["profiles"]:
            print("Inga profiler finns. Skapar ny profil...")
            return self.create_profile()
        
        name = input("Ange användarnamn: ").strip()
        if name not in self.profiles["profiles"]:
            print("Profilen hittades inte.")
            return None
        while True:
            password = getpass.getpass("Ange lösenord: ").strip()
            hashed_input = hashlib.sha256(password.encode()).hexdigest()
            if hashed_input == self.profiles["profiles"][name]["password"]:

                print(f"Välkommen tillbaka, {name}!\n")
                self.logged_in_user = name
                return name
            else:
                print("Fel lösenord. Försök igen.")

    def logout(self):
        if self.logged_in_user:
            print(f"{self.logged_in_user} har loggats ut.")
            self.logged_in_user = None
        else:
            print("Ingen användare är inloggad.")

    def show_logged_in(self):
        if self.logged_in_user:
            print(f"Inloggad som: {self.logged_in_user}")
        else:
            print("Ingen användare inloggad.")

    def is_logged_in(self):
        return self.logged_in_user is not None


    def add_points(self, points):
        if not self.logged_in_user:
            print("Ingen användare är inloggad.")
            return
        
        self.profiles["profiles"][self.logged_in_user]["points"] += points
        self.save_profiles()
        print(f"{points} poäng har lagts till för {self.logged_in_user}!")

    def show_points(self):
        if not self.logged_in_user:
            print("Ingen användare är inloggad.")
            return
        
        points = self.profiles["profiles"][self.logged_in_user]["points"]
        print(f"{self.logged_in_user} har {points} poäng.")

    def add_result(self, correct, total):
        """Add results from a round to the logged-in account."""
        if not self.logged_in_user:
            print("Ingen användare är inloggad.")
            return
        
        profile = self.profiles["profiles"][self.logged_in_user]
        profile["points"] += correct
        profile["attempts"] = profile.get("attempts", 0) + total
        self.save_profiles()
        print(f"{correct} poäng lagts till för {self.logged_in_user} ({profile['points']} totalt, {profile['attempts']} försök totalt)")



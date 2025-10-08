users = {}
username = input()
password = input()
if username in users and users [username] == password:
    print("inloggning lyckades", username)
else:
    print("inloggning misslyckades felanvänarnamn eller lösenord")



class Loggin:
    def __init__(self):
        self.users = []
    
    def register(self):
        print("ny användare")
        username = input("välj användarnamn")
        if username in self.users:
            print("användare finns redan")
            return
        password = input("välj lösenord").strip()
        self.users[username] = password
        print("inloggning lyckades =)")

    def loin(self):
        print("Logga in")
        username = input("Användarnamn: ")
        password = input("Lösenord: ")

        if username in self.users and self.users[self.users]== password:
                print(f"inloggning lyckades välkommen {username}")
                return True
        else:
            print("inloggning misslyckades fel användarnamn eller lösenord")
        return False

class Login:
    def __init__(self):
        self.users = {}  # använd ett dictionary istället för lista

    def register(self):
        print("\n📋 Registrera ny användare")
        username = input("Välj användarnamn: ").strip().lower()
        if username in self.users:
            print("❌ Användare finns redan")
            return
        password = input("Välj lösenord: ").strip()
        self.users[username] = password
        print("✅ Registrering lyckades! Du kan nu logga in.")

    def login(self):
        print("\n🔐 Logga in")
        username = input("Användarnamn: ").strip().lower()
        password = input("Lösenord: ").strip()

        if username in self.users and self.users[username] == password:
            print(f"✅ Inloggning lyckades, välkommen {username}!")
            return True
        else:
            print("❌ Inloggning misslyckades – fel användarnamn eller lösenord")
            return False

# -----------------------------
# Test-spel
# -----------------------------
log = Login()

while True:
    print("\n1. Registrera ny användare")
    print("2. Logga in")
    print("3. Avsluta")
    choice = input("Välj: ").strip()

    if choice == "1":
        log.register()
    elif choice == "2":
        if log.login():
            # Enkel test-loop efter login
            score = 0
            running = True
            print("\n🎮 Spelet startar! Skriv 'q' för att avsluta")
            while running:
                action = input("Tryck 'a' för poäng, 'q' för att sluta: ").lower().strip()
                if action == "a":
                    score += 1
                    print(f"Du fick 1 poäng! Total poäng: {score}")
                elif action == "q":
                    print(f"Spelet avslutas. Din slutpoäng: {score}")
                    running = False
                else:
                    print("Ogiltigt val, försök igen.")
            break
    elif choice == "3":
        print("👋 Avslutar programmet")
        break
    else:
        print("Ogiltigt val, försök igen")
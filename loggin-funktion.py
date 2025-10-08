users = {}
username = input()
password = input()
if username in users and users [username] == password:
    print("inloggning lyckades", username)
else:
    print("inloggning misslyckades felanvänarnamn eller lösenord")

running = True
score = 0

print("🎮 Välkommen till spelet!")
print("Skriv 'q' för att avsluta.\n")

while running:
    print("Du spelar spelet...")
    print(f"Din poäng: {score}")
    
    # Exempel på något som händer i spelet
    action = input("Tryck 'a' för att få poäng eller 'q' för att avsluta: ").lower().strip()
    
    if action == "a":
        score += 1
        print("Du fick 1 poäng!\n")
    elif action == "q":
        print(f"Spelet avslutas. Du fick totalt {score} poäng.")
        running = False
    else:
        print("Ogiltigt val, försök igen.\n")

# main.py
from core.game_loop import GameLoop
from core.login import Account
from core.scoreboard import Scoreboard

def main_menu():
    game = GameLoop()
    account = Account()
    scoreboard = Scoreboard()
    while True:
        print("\n=== Huvudmeny ===")
        print("1. Spela")
        print("2. Visa poängtavla")
        print("3. Logga in / Registrera")
        print("4. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            game.start_round()
        elif choice == "2":
            scoreboard.show_top_scores()
        elif choice == "3":
            if not account.is_logged_in():
                account.login()
            else:
                account.logout()
        elif choice == "4":
            print("Hejdå!")
            break
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    main_menu()

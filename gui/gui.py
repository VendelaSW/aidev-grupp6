import customtkinter as ctk
import hashlib
from core.login import Account
from core.game_loop import GameLoop
from core.scoreboard import Scoreboard
import time

class MainMenu(ctk.CTkFrame):
    def __init__(self, master, switch_frame, account):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.account = account

        # Configure grid for centering
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Wrapper frame to center title and buttons
        center_frame = ctk.CTkFrame(self, fg_color="transparent")
        center_frame.grid(row=2, column=1, sticky="nsew")
        
        # Title label
        self.title_label = ctk.CTkLabel(center_frame, text="Huvudmeny", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=(0, 20))

        # Buttons
        self.play_button = ctk.CTkButton(
            center_frame, 
            text="Spela", 
            command=lambda: self.start_game_window(switch_frame)
            )
        self.scoreboard_button = ctk.CTkButton(center_frame, text="Scoreboard", command=lambda: switch_frame("score"))
        self.quit_button = ctk.CTkButton(center_frame, text="Avsluta", command=master.quit)

        # Layout
        self.play_button.pack(pady=5)
        self.scoreboard_button.pack(pady=5)
        self.quit_button.pack(pady=5)

        # Username label (top-right)
        self.username_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.username_label.place(relx=1.0, rely=0.0, anchor="ne", x=-100, y=10)  # adjust x for spacing

        # Account button in top-right corner (separate)
        self.account_button = ctk.CTkButton(self, text="Logga in", width=80, height=30, command=lambda: switch_frame("account"))
        self.account_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
    
    def start_game_window(self, switch_frame):
        switch_frame("game")
        self.master.frames["game"].start_game()

    def refresh_account_button(self):
        if self.account.is_logged_in():
            user = self.account.logged_in_user
            self.username_label.configure(text=f"Inloggad som: {user}")
            self.account_button.configure(text="Logga ut", command=self.logout)
        else:
            self.username_label.configure(text="")
            self.account_button.configure(text="Logga in", command=lambda: self.switch_frame("account"))

    def logout(self):
        self.account.logged_in_user = None
        self.refresh_account_button()

class GameWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame, game):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.game = game

        # Make the entire grid expandable
        for i in range(4):  # 4 rows: title, option row 1, option row 2, back button
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):  # 2 columns
            self.grid_columnconfigure(i, weight=1)

        # Question label
        self.question_label = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=20)

       # Option buttons
        self.option_buttons = []
        for i in range(4):
            btn = ctk.CTkButton(self, text="", command=lambda i=i: self.answer_selected(i))
            self.option_buttons.append(btn)
            row = 1 + i // 2
            col = i % 2
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew") 

        # Back to menu button
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=3, column=0, columnspan=2, pady=20)

    def start_game(self):
        self.game.start_new_game()
        self.start_time = time.time()

        # Reset question label and button colors
        self.question_label.configure(text="")
        default_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]

        for btn in self.option_buttons:
            btn.grid()
            btn.configure(text="", fg_color=default_color, state="normal")

        self.show_question()


    def show_question(self):
        q = self.game.get_current_question()
        if not q:
            self.show_results()
            return

        self.question_label.configure(text=q["question"])
        options = q.get("options", [])
        default_color = ctk.ThemeManager.theme["CTkButton"]["fg_color"]
        for i, btn in enumerate(self.option_buttons):
            btn.configure(fg_color=default_color, state="normal")
            if i < len(options):
                btn.configure(text=options[i], state="normal")
            else:
                btn.configure(text="", state="disabled")

    def answer_selected(self, index):
        q = self.game.get_current_question()
        if not q:
            return
        answer = self.option_buttons[index].cget("text")
        correct, done = self.game.submit_answer(answer)

        # Feedback color
        if correct:
            self.option_buttons[index].configure(fg_color="green")
        else:
            self.option_buttons[index].configure(fg_color="red")

        self.after(1500, lambda: self.next_question(done))

    def next_question(self, done):
        if done:
            self.show_results()
        else:
            self.show_question()

    def show_results(self):
        # Hide option buttons
        for btn in self.option_buttons:
            btn.grid_remove()

        # Show result text
        self.question_label.configure(
            text=f"Du fick {self.game.score}/{len(self.game.questions)} rätt!"
        )

        # End time for the game
        self.game.end_time = time.time()
        elapsed = self.game.end_time - self.start_time

        # Access account and scoreboard
        account = self.master.frames["menu"].account  # your logged-in account
        scoreboard = self.master.frames["score"].scoreboard  # your Scoreboard instance

        # Save the score
        scoreboard.save_score(
            account,
            self.game.score,
            len(self.game.questions),
            elapsed
        )



class ScoreboardWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame, scoreboard):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.scoreboard = scoreboard

        self.grid_rowconfigure(0, weight=1)  # title
        self.grid_rowconfigure(1, weight=5)  # scores
        self.grid_rowconfigure(2, weight=1)  # back button
        self.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self, text="Top Scoreboard", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, pady=10)

        # Scores frame (scrollable if needed later)
        self.scores_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.scores_frame.grid(row=1, column=0, sticky="ns")

        # Back to menu
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=2, column=0, pady=10)

    def update_scores(self):
        # Clear previous labels
        for widget in self.scores_frame.winfo_children():
            widget.destroy()

        top_scores = self.scoreboard.get_top_scores(5)  # new method returns list of dicts
        if not top_scores:
            lbl = ctk.CTkLabel(self.scores_frame, text="Inga poäng sparade ännu!")
            lbl.pack(pady=5)
            return

        for i, entry in enumerate(top_scores, 1):
            name = entry["name"]
            score = entry["score"]
            total = entry["total"]
            accuracy = entry["accuracy"]
            time = entry["time"]
            lbl = ctk.CTkLabel(
                self.scores_frame,
                text=f"{i}. {name}: {score}/{total} ({accuracy:.1f}% korrekt) på {time:.1f}s"
            )
            lbl.pack(anchor="w", pady=2, padx=10)

class AccountWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame, account):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.account = account
        

        self.grid_rowconfigure(0, weight=1)  # Title
        self.grid_rowconfigure(1, weight=0)  # Username entry
        self.grid_rowconfigure(2, weight=0)  # Password label
        self.grid_rowconfigure(3, weight=0)  # Password entry
        self.grid_rowconfigure(4, weight=0)  # Bottom expands
        self.grid_rowconfigure(5, weight=1)
        for i in range(2):  # 2 columns
            self.grid_columnconfigure(i, weight=1)

        # Question label
        self.username_label = ctk.CTkLabel(self, text="Username: ", font=("Arial", 16))
        self.username_label.grid(row=0, column=0, columnspan=2, pady=0, sticky="s")

        # Question label
        self.password_label = ctk.CTkLabel(self, text="Password: ", font=("Arial", 16))
        self.password_label.grid(row=2, column=0, columnspan=2, pady=0, sticky="s")

        # Login entry
        self.username_entry = ctk.CTkEntry(self, )
        self.username_entry.grid(row=1, column=0, columnspan= 2, pady=0, sticky="n")
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=3, column=0, columnspan= 2, pady=0, sticky="n")

        # Feedback label
        self.feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.feedback_label.grid(row=5, column=0, columnspan=2, pady=(5,5), sticky="s")

        # Login button
        self.login_button = ctk.CTkButton(self, text="Logga in", command=self.try_login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=(5, 0), sticky="s")

        # Register button
        self.register_button = ctk.CTkButton(
        self, 
        text="Registrera nytt konto", 
        command=lambda: switch_frame("register")
        )
        self.register_button.grid(row=5, column=0, columnspan=2, pady=(5, 5), sticky="n")

        # Back to menu button
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=6, column=0, columnspan=2, pady=(0, 20), sticky="n")

        self.username_entry.bind("<Return>", lambda event: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda event: self.try_login())

    def try_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            self.feedback_label.configure(text="Fyll i både användarnamn och lösenord", text_color="red")
            return

        if username in self.account.profiles["profiles"]:
            hashed_input = hashlib.sha256(password.encode()).hexdigest()
            if hashed_input == self.account.profiles["profiles"][username]["password"]:
                self.account.logged_in_user = username
                self.feedback_label.configure(text=f"Välkommen, {username}!", text_color="green")
                self.after(500, lambda: [self.switch_frame("menu"), self.master.frames["menu"].refresh_account_button()])
                return

        self.feedback_label.configure(text="Fel användarnamn eller lösenord", text_color="red")

    def try_register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            self.feedback_label.configure(text="Fyll i både användarnamn och lösenord", text_color="red")
            return

        if username in self.account.profiles["profiles"]:
            self.feedback_label.configure(text="Användarnamnet finns redan", text_color="red")
            return

        self.account.profiles["profiles"][username] = {
            "password": hashlib.sha256(password.encode()).hexdigest(),
            "points": 0,
            "attempts": 0
        }
        self.account.save_profiles()
        self.feedback_label.configure(text=f"Konto skapades för {username}", text_color="green")
        self.after(500, lambda: [self.switch_frame("menu"), self.master.frames["menu"].refresh_account_button()])

    def reset(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.feedback_label.configure(text="")

class RegisterWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame, account):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.account = account
        


        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Skapa konto", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, pady=10)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Användarnamn")
        self.username_entry.grid(row=1, column=0, pady=5, padx=40, sticky="ew")

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Lösenord", show="*")
        self.password_entry.grid(row=2, column=0, pady=5, padx=40, sticky="ew")

        self.confirm_entry = ctk.CTkEntry(self, placeholder_text="Bekräfta lösenord", show="*")
        self.confirm_entry.grid(row=3, column=0, pady=5, padx=40, sticky="ew")

        self.feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 14))
        self.feedback_label.grid(row=4, column=0, pady=5)

        self.register_button = ctk.CTkButton(self, text="Skapa konto", command=self.try_register)
        self.register_button.grid(row=5, column=0, pady=10)

        self.back_button = ctk.CTkButton(self, text="Tillbaka", command=lambda: switch_frame("account"))
        self.back_button.grid(row=6, column=0, pady=10)

        self.username_entry.bind("<Return>", lambda event: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda event: self.confirm_entry.focus())
        self.confirm_entry.bind("<Return>", lambda event: self.try_register())

    def try_register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()

        if not username or not password or not confirm:
            self.feedback_label.configure(text="Fyll i alla fält", text_color="red")
            return
        if password != confirm:
            self.feedback_label.configure(text="Lösenorden matchar inte", text_color="red")
            return
        if username in self.account.profiles["profiles"]:
            self.feedback_label.configure(text="Användarnamnet finns redan", text_color="red")
            return

        # Hash password and save
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.account.profiles["profiles"][username] = {
            "password": hashed,
            "points": 0,
            "attempts": 0
        }
        self.account.save_profiles()
        self.feedback_label.configure(text=f"Konto skapat för {username}", text_color="green")

        # Go back to login after short delay
        self.after(1000, lambda: self.switch_frame("account"))

    def reset(self):
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_entry.delete(0, "end")
        self.feedback_label.configure(text="")

        # Make sure placeholders stay visible
        self.username_entry.configure(placeholder_text="Användarnamn")
        self.password_entry.configure(placeholder_text="Lösenord")
        self.confirm_entry.configure(placeholder_text="Bekräfta lösenord")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyKodMiljonären")
        self.geometry("400x300")
        account = Account()
        game = GameLoop()
        scoreboard = Scoreboard()

        # ✅ Store them in the App instance so other frames can access them
        self.account = account
        self.game = game
        self.scoreboard = scoreboard

        self.frames = {}
        self.create_frames(account, game, scoreboard)
        self.show_frame("menu")

    def create_frames(self, account, game, scoreboard):
        self.frames["menu"] = MainMenu(self, self.show_frame, account)
        self.frames["game"] = GameWindow(self, self.show_frame, game)
        self.frames["score"] = ScoreboardWindow(self, self.show_frame, scoreboard)
        self.frames["account"] = AccountWindow(self, self.show_frame, account)
        self.frames["register"] = RegisterWindow(self, self.show_frame, account)
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

        # Optional: resize window based on frame
        if name == "game":
            self.geometry("1080x400")  # width x height
        elif name == "menu":
            self.geometry("400x300")
        elif name == "score":
            self.geometry("500x400")
            frame.update_scores()  # refresh scores whenever the frame is shown
        elif name == ("account", "register"):
            frame.reset()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()
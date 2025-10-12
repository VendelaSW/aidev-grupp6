import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

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
        self.play_button = ctk.CTkButton(center_frame, text="Spela", command=lambda: switch_frame("game"))
        self.scoreboard_button = ctk.CTkButton(center_frame, text="Scoreboard", command=lambda: switch_frame("score"))
        self.quit_button = ctk.CTkButton(center_frame, text="Avsluta", command=master.quit)

        # Layout
        self.play_button.pack(pady=5)
        self.scoreboard_button.pack(pady=5)
        self.quit_button.pack(pady=5)

        # Account button in top-right corner (separate)
        self.account_button = ctk.CTkButton(self, text="Logga in", width=80, height=30, command=lambda: switch_frame("account"))
        self.account_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
     


class GameWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        # Make the entire grid expandable
        for i in range(4):  # 4 rows: title, option row 1, option row 2, back button
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):  # 2 columns
            self.grid_columnconfigure(i, weight=1)

        # Question label
        self.question_label = ctk.CTkLabel(self, text="Here is the question", font=("Arial", 16))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=20)

       # Option buttons
        self.option_buttons = []
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        for i, option_text in enumerate(options):
            btn = ctk.CTkButton(self, text=option_text)
            self.option_buttons.append(btn)
            row = 1 + i // 2  # first two buttons in row 1, next two in row 2
            col = i % 2       # first button col 0, second col 1, etc.
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew") 

        # Back to menu button
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=3, column=0, columnspan=2, pady=20)

class ScoreboardWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        # Make the entire grid expandable
        for i in range(4):  # 4 rows: title, option row 1, option row 2, back button
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):  # 2 columns
            self.grid_columnconfigure(i, weight=1)

        # Back to menu button
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=3, column=0, columnspan=2, pady=20)

class AccountWindow(ctk.CTkFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame

        # Make the entire grid expandable
        for i in range(4):  # 4 rows: title, option row 1, option row 2, back button
            self.grid_rowconfigure(i, weight=1)
        for i in range(2):  # 2 columns
            self.grid_columnconfigure(i, weight=1)

        # Back to menu button
        self.back_button = ctk.CTkButton(self, text="Tillbaka till meny", command=lambda: switch_frame("menu"))
        self.back_button.grid(row=3, column=0, columnspan=2, pady=20)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PyKodMiljonären")
        self.geometry("400x300")

        self.frames = {}
        self.create_frames()
        self.show_frame("menu")

    def create_frames(self):
        self.frames["menu"] = MainMenu(self, self.show_frame)
        self.frames["game"] = GameWindow(self, self.show_frame)
        self.frames["score"] = ScoreboardWindow(self, self.show_frame)
        self.frames["account"] = AccountWindow(self, self.show_frame)
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()
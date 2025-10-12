from gui.gui import App
import customtkinter as ctk

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Optional: dark theme
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()
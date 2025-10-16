# 🧠 Quiz Game Project  

A quiz game with user profiles, a scoreboard, and both GUI and CLI support.  
Built as a school project to practice Python programming, teamwork, and object-oriented design.

---

## 🎯 Purpose  
This project was created as part of our Python course to practice:
- Object-Oriented Programming (OOP)
- File handling and JSON data storage  
- Error handling and testing with `pytest`  
- GUI development using `Tkinter` and `customtkinter`  
- Team collaboration using Git and GitHub  

---

## 🧩 Features  
- 🔐 Login system with user profiles  
- 🧠 Multiple quiz categories (music, geography, sports, psychology, etc.)  
- 🏆 Scoreboard saved between sessions  
- 💾 JSON-based data management  
- 🎨 Graphical interface (GUI) built with Tkinter  
- 💻 Optional CLI version for testing or fallback use  
- ✅ Unit testing using `pytest`  

---

## ⚙️ Installation  

Clone the repository and install dependencies:
bash
git clone git@github.com:VendelaSW/aidev-grupp6.git
cd aidev-grupp6.git
pip install -r requirements.txt

---

Run the game with python main.py

---

| Name         | Role           | Contribution                                          |
| ------------ | -------------- | ----------------------------------------------------- |
| Vendela      | Lead Developer | Game loop, GUI integration, structure, git management |
| Adam         | Developer      | Scoreboard, Geography Questions                       |
| Kevin        | Developer      | Login, profile handling, Sports Questions             |
| Joshua       | Developer      | Investment Questions                                  |
| Spirit       | Developer      | Communications, merge conflicts, Psychology Questions |

---
## Folder Structure
aidev-grupp6/
├── README.md
├── core
│   ├── __init__.py
│   ├── game_loop.py
│   ├── login.py
│   ├── menu.py
│   └── scoreboard.py
├── data
│   ├── results_data.json
│   └── user_data.json
├── exempel-format.py
├── exempel-upplägg.md
├── gui
│   ├── __init__.py
│   └── gui.py
├── main.py
├── questions
│   ├── __init__.py
│   ├── geography_questions.py
│   ├── investment_questions.py
│   ├── music_questions.py
│   ├── psychology_questions.py
│   ├── questions_class.py
│   └── sport_questions.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_game_loop.py
    ├── test_investment_questions.py
    ├── test_psychology_questions.py
    └── test_sport_questions.py

---

We learned how to:

- Structure a Python project into modules

- Use OOP and inheritance in practical scenarios

- Work with JSON for data persistence

- Collaborate using Git and GitHub

- Write basic pytest tests for core functionality

The most challenging part was connecting the GUI to the underlying logic without breaking the game flow.
Overall, we’re proud of the result and how our teamwork evolved throughout the project.

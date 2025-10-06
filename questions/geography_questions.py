import random

class GeographyQuiz:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "Which is the largest country in the world by area?",
                "options": ["Canada", "USA", "Russia", "China"],
                "correct_answer": "Russia"
            },
            {
                "question": "What is the longest river in the world?",
                "options": ["Nile", "Amazon River", "Yangtze", "Mississippi"],
                "correct_answer": "Nile"
            },
            {
                "question": "Which country has the largest population in the world?",
                "options": ["India", "USA", "China", "Indonesia"],
                "correct_answer": "India"
            },
            {
                "question": "What is the capital city of Canada?",
                "options": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
                "correct_answer": "Ottawa"
            },
            {
                "question": "On which continent is the Sahara Desert located?",
                "options": ["Asia", "Africa", "Australia", "South America"],
                "correct_answer": "Africa"
            },
            {
                "question": "Which country consists of the most islands?",
                "options": ["Indonesia", "Philippines", "Japan", "Sweden"],
                "correct_answer": "Sweden"
            },
            {
                "question": "Which ocean lies east of Africa?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Mediterranean Sea"],
                "correct_answer": "Indian Ocean"
            },
            {
                "question": "What is the highest mountain in Europe?",
                "options": ["Mont Blanc", "Matterhorn", "Elbrus", "Kebnekaise"],
                "correct_answer": "Elbrus"
            },
            {
                "question": "In which country are the Pyramids of Giza located?",
                "options": ["Mexico", "Egypt", "Sudan", "Jordan"],
                "correct_answer": "Egypt"
            },
            {
                "question": "What is the largest island in the world?",
                "options": ["Greenland", "New Guinea", "Borneo", "Madagascar"],
                "correct_answer": "Greenland"
            }
        ]
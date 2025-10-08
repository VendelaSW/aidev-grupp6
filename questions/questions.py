import random

class Question:
    def __init__(self):
        self.questions = []
    
    def get_random_question(self):
        return random.choice(self.questions)
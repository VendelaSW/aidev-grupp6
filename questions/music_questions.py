import random

class MusicQuestions:
    def __init__(self):
        self.questions = [
    {"question": "Vilka artister hade 2020-talets största beef?", 
     "options": ["A) Pusha T och Tyler the creator", "B) Kanye 'Ye' West och Lil Dicky",
                 "C) Kendrick lamar och Drake", "D) Weird Al Yankovich och Chamillionaire"], 
     "answer": "C) Kendrick lamar och Drake"},
    
    {"question": "Fråga 2: Vilken artist släppte låten 'Doja Cat'?", 
     "options": ["A) Harry Styles", "B) Doja Cat",
                 "C) Kanye 'Ye' West", "D) Central Cee"], 
     "answer": "D) Central Cee"},
    
    {"question": "Fråga 3: Vilken pop stjärna håller rekordet för flest veckor som nummer 1 på Billboard Hot 100 med en enda låt?", 
     "options": ["A) Luis Fonsi & Daddy Yankee ft. Justin Bieber - Despacito", "B) Ed Sheeran - Shape of you",
                 "C) Lil Nas X ft Billy Ray Cyrus - Old Town Road", "D) Mariah Carey & Boyz II Men - One sweet day"], 
     "answer": "C) Lil Nas X ft Billy Ray Cyrus - Old Town Road"},
    
    {"question": "Fråga 4: 2022 släppte Jack Harlow sin virala låt First Class som sampler denna tidigt 2000-tals hit låt.", 
     "options": ["A) Gwen Stefani - Hollaback Girl", "B) Fergie - Glamorous",
                 "C) Nelly Furtado - Promiscuous", "D) Beyoncé - Crazy in Love"], 
     "answer": "B) Fergie - Glamorous"},
    
    {"question": "Fråga 5: Vilket bands frontman vart kallad 'the voice of a generation' efter att de släppte sitt 1991 album Nevermind?", 
     "options": ["A) Pearl Jam", "B) Nirvana", "C) Soundgarden", "D) Smashing Pumpkins"], 
     "answer": "B) Nirvana"},
    
    {"question": "Fråga 6: Vilket 2000-tals rockband samplade från en James Bond-film?", 
     "options": ["A) The White Stripes", "B) System of a Down", "C) Linkin Park", "D) My Chemical Romance"], 
     "answer": "C) Linkin Park"},
    
    {"question": "Fråga 7: Vilket Heavy Metal-band blev stämda på 90-talet för att ha haft undermedvetna meddelanden i deras låtar, vilket ledde till att ett fan dog?", 
     "options": ["A) Metallica", "B) Judas Priest", "C) Slayer", "D) Black Sabbath"], 
     "answer": "B) Judas Priest"},
    
    {"question": "Fråga 8: Vad var Ozzy Osbournes smeknamn?", 
     "options": ["A) The King of Metal", "B) The God of Rock n Roll", "C) The Prince of Darkness", "D) The Mad Blizzard"], 
     "answer": "C) The Prince of Darkness"},
    
    {"question": "Fråga 9: Vilken Reggae-legend begravdes med hans gitarr, en bibel, en ring, och en marijuanaknopp?", 
     "options": ["A) Peter Tosh", "B) Bob Marley", "C) Jimmy Cliff", "D) Toots Hibbert"], 
     "answer": "B) Bob Marley"},
    
    {"question": "Fråga 10: Vilken Jazzmusiker är känd för att ha varit pionjär inom bebop tillsammans med Charlie Parker på 40-talet?", 
     "options": ["A) Louis Armstrong", "B) Dizzy Gillespie", "C) Duke Ellington", "D) Miles Davis"], 
     "answer": "B) Dizzy Gillespie"}
    ]

    def get_random_question(self):
        return random.choice(self.questions)
    
    def check_answer(self, question, user_answer):
        return user_answer.strip().lower() == question["answer"].lower()
    
    def print_all_questions(self):
        for q in self.questions:
            print(q["question"])

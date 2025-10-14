# Vill testa funktionen check_answer() i min Psychology-klass
# Och säkerställa att rätt och fel svar hanteras korrekt.

import pytest
from questions.psychology_questions import Psychology

def test_check_answer_correct():
    # Testa att funktionen returnerar True om svaret är rätt
    quiz = Psychology()
    question = quiz.questions[0]  
    assert quiz.check_answer(question, "D") is True 

def test_check_answer_incorrect():
    """Testar att funktionen returnerar False om svaret är fel"""
    quiz = Psychology()
    question = quiz.questions[0]
    assert quiz.check_answer(question, "A") is False 
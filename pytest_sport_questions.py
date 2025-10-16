import pytest
from sport_question import SportQuestion

def test_number_of_questions():
    """Testar att vi har 10 frågor"""
    q = SportQuestion()
    assert len(q.questions) == 10

def test_random_question_answer_valid():
    """Testar att random_question returnerar ett giltigt svar"""
    q = SportQuestion()
    # Kör random_question flera gånger för att täcka flera frågor
    for _ in range(10):
        answer = q.random_question()
        # Rätt svar ska alltid vara en av 'a', 'b', 'c', 'd' (små bokstäver)
        assert answer.lower() in ["a", "b", "c", "d"]

def test_question_structure():
    """Testar att varje fråga har rätt struktur"""
    q = SportQuestion()
    for question in q.questions:
        assert "question" in question
        assert "options" in question
        assert "answer" in question
        # Options måste vara en lista med minst 2 element
        assert isinstance(question["options"], list)
        assert len(question["options"]) >= 2
        # Answer måste finnas i options
        valid_answers = [opt[0].lower() for opt in question["options"]]  # A, B, C, D → a, b, c, d
        assert question["answer"].lower() in valid_answers

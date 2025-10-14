# tests/test_investment_questions.py
# Tester för InvestmentQuestions (pytest)

from investment_questions import InvestmentQuestions

def test_class_creation():
    # Testar att klassen kan skapas korrekt
    quiz = InvestmentQuestions()
    assert isinstance(quiz, InvestmentQuestions)
    assert isinstance(quiz.questions, list)

def test_questions_not_empty():
    # Testar att listan med frågor inte är tom
    quiz = InvestmentQuestions()
    assert len(quiz.questions) > 0

def test_question_structure():
    # Testar att varje fråga har rätt struktur: "question", "options", "answer"
    quiz = InvestmentQuestions()
    first = quiz.questions[0]
    assert "question" in first
    assert "options" in first
    assert "answer" in first

def test_options_are_list_and_count():
    # Testar att varje fråga har en lista med exakt 4 alternativ
    quiz = InvestmentQuestions()
    for q in quiz.questions:
        assert isinstance(q["options"], list)
        assert len(q["options"]) == 4

def test_answer_format():
    # Testar att svaret är en sträng och har format som t.ex. "B) Spotify"
    quiz = InvestmentQuestions()
    for q in quiz.questions:
        ans = q["answer"]
        assert isinstance(ans, str)
        assert ")" in ans

def test_no_empty_strings():
    # Testar att det inte finns tomma strängar i frågor, svar eller alternativ
    quiz = InvestmentQuestions()
    for q in quiz.questions:
        assert q["question"].strip() != ""
        assert q["answer"].strip() != ""
        for opt in q["options"]:
            assert opt.strip() != ""

def test_play_exists():
    # Testar att metoden play finns i klassen
    quiz = InvestmentQuestions()
    assert hasattr(quiz, "play")
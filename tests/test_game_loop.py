import pytest
from core.game_loop import GameLoop

@pytest.fixture
def game():
    return GameLoop()

def test_start_new_game(game):
    game.start_new_game()
    assert len(game.questions) > 0, "Questions should be generated"
    assert game.score == 0
    assert game.current_index == 0

def test_get_current_question(game):
    game.start_new_game()
    q = game.get_current_question()
    assert isinstance(q, dict), "Should return a dictionary"
    assert "question" in q

def test_submit_answer_correct(game):
    game.start_new_game()
    q = game.get_current_question()
    correct_answer = q.get("answer", "")
    result, done = game.submit_answer(correct_answer)
    assert result is True
    assert game.score == 1
    assert isinstance(done, bool)

def test_submit_answer_incorrect(game):
    game.start_new_game()
    result, done = game.submit_answer("nonsense answer")
    assert result is False

def test_get_question_from_category(game):
    from questions.music_questions import MusicQuestions
    q = game.get_question_from_category(MusicQuestions())
    assert isinstance(q, dict)
    assert "question" in q
    assert "answer" in q or "correct_answer" in q

def test_get_current_question_out_of_range(game):
    game.start_new_game()
    game.current_index = 999  # beyond range
    assert game.get_current_question() is None

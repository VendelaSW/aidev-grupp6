import json
import pytest
from core.scoreboard import Scoreboard

# ------------------------
# Mockad Account-klass
# ------------------------
class MockAccount:
    def __init__(self, logged_in=True, username="TestUser"):
        self._logged_in = logged_in
        self.logged_in_user = username

    def is_logged_in(self):
        return self._logged_in

# ------------------------
# Fixtures
# ------------------------
@pytest.fixture
def temp_score_file(tmp_path):
    """Skapar en temporär JSON-fil för testet"""
    return tmp_path / "test_results.json"

@pytest.fixture
def logged_in_account():
    """Mockad inloggad användare"""
    return MockAccount(logged_in=True, username="Alice")

@pytest.fixture
def logged_out_account():
    """Mockad utloggad användare"""
    return MockAccount(logged_in=False)

# ------------------------
# Tester
# ------------------------
def test_save_scores(temp_score_file, logged_in_account, logged_out_account, capsys):
    sb = Scoreboard(filename=temp_score_file)

    # Spara poäng med inloggad användare
    sb.save_score(logged_in_account, score=8, total=10, time=25)
    
    # Försök spara med utloggad användare (ska inte sparas)
    sb.save_score(logged_out_account, score=5, total=10, time=30)

    # Läs filen
    with open(temp_score_file, "r") as f:
        data = json.load(f)

    # Endast den inloggade användarens resultat ska sparas
    assert len(data) == 1
    assert data[0]["name"] == "Alice"
    assert data[0]["score"] == 8

def test_get_top_scores(temp_score_file, logged_in_account):
    sb = Scoreboard(filename=temp_score_file)
    
    # Spara flera rundor för samma användare
    sb.save_score(logged_in_account, 5, 10, 20)
    sb.save_score(logged_in_account, 7, 10, 25)
    
    top_scores = sb.get_top_scores()
    
    # Endast högsta poängen ska räknas
    assert len(top_scores) == 1
    assert top_scores[0]["score"] == 7
    assert top_scores[0]["name"] == "Alice"

def test_show_top_scores_output(temp_score_file, logged_in_account, capsys):
    sb = Scoreboard(filename=temp_score_file)
    
    # Spara några poäng
    sb.save_score(logged_in_account, 6, 10, 15)
    sb.save_score(logged_in_account, 9, 10, 20)
    
    # Visa top scores
    sb.show_top_scores()
    
    output = capsys.readouterr().out
    assert "SCOREBOARD" in output
    assert "Alice" in output
    assert "9/10" in output

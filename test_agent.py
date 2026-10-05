from agent import create_team

def test_team_creation():
    team=create_team()

    assert team is not None
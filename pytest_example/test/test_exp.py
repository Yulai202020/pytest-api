from src import main

def test_exp():
    res: int = main.exp(4,2)
    assert res == 16
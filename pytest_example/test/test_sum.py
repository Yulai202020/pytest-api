from src import main

def test_sum():
    res: int = main.sum(1,3)
    assert res == 4
from src import main

def test_mult():
    res: int = main.mult(2,3)
    assert res == 6
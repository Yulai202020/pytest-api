from src import main

def test_sub():
    res: int = main.sub(10,2)
    assert res == 8
from src import main

def test_dvn():
    res: int = main.dvn(4,2)
    assert res == 2
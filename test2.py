from add import add

def tests():
    test_add()
    test_add_2()

def test_add():
    assert add(1,2) == 3

def test_add_2():
    assert add(1,2) == 1

if __name__ == "__main__":
    tests()
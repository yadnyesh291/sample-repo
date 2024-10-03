import pytest
from my_module import my_function

def test_my_function():
    assert my_function(3) == 9
    assert my_function(0) == 0
    assert my_function(-1) == 1

if __name__ == "__main__":
    pytest.main()
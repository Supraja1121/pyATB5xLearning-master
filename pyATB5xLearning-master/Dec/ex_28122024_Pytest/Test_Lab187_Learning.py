import pytest

@pytest.mark.smoke
def method1():
    print("test1")
    assert 1-1 == 2


@pytest.mark.smoke
def method2():
    print("test2")
    assert 1-1 == 0
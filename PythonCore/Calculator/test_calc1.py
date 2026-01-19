from Calculator.Calc import add,divide
import pytest
def test_add_positive():
    assert 2 + 3 == 5
def test_list(): 
    assert 3 in [1, 2, 3]
    assert [1,2,3]==[1,2,3]
    assert {'a':1,'b':2}=={'b':2,'a':1}
def test_tuple_equal():
    assert (1,2)==(1,2)
def test_set_equal():
    assert {1,2,3}=={3,2,1}
def test_float():
     assert 10.01 == pytest.approx(10.0, abs=0.05)
def test_add_negative():
    assert add(2,-5) == -3
def test_nested():
    assert {
        "user": {"name": "Alice", "age": 25},
        "roles": ["admin", "user"]
    } == {
        "user": {"name": "Alice", "age": 25},
        "roles": ["admin", "user"]
    }
def test_index_error():
    with pytest.raises(IndexError):
        [1, 2, 3][9]
def test_exception():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)

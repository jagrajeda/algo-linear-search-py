from linear_search import linear_search,linear_search_global
import pytest

def test_linear_search_exists():
    assert linear_search(3, [1,2,3]) == 2

def test_linear_search_does_not_exist():
    assert linear_search(4, [1,2,3]) == None

def test_linear_search_each_int_exists_but_not_whole():
    assert linear_search(13, [1,2,3]) == None


# tests for linear_search_global
def test_global_search_multiple_chars():
    assert linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]

def test_global_search_single_char():
    assert linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6]

def test_global_search_duplicate_char():
    assert linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4]

# I wasn't sure if we needed to add more tests here so I'll first try running with the pre-filled ones
# now I'm adding my edge cases - I see we don't yet have some with empty list so I wil create some

def test_linear_search_empty_array():
    assert linear_search(1, []) == None

def test_global_search_not_found():
    assert linear_search_global("z", ["a", "b", "c"]) == []

# all right and my two edge cases passed as well - Noice!
import pytest

def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(6) == 720
    assert factorial(8) != 40000
    with pytest.raises(ValueError):
        assert factorial(-1)
    with pytest.raises(TypeError):
        assert factorial("test")
        assert factorial(3.5)

def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurrence_in_string():
    assert count_word_occurrence_in_string("one two one", "one") == 2
    assert count_word_occurrence_in_string("one two one", "four") == 0
    assert count_word_occurrence_in_string("one two one", "o") == 0 
    assert count_word_occurrence_in_string("one, two, three", "one") == 0 # technically it should be 1

def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

def test_count_word_occurrence_in_file():
    assert count_word_occurrence_in_file("test.txt", "one") == 2
    assert count_word_occurrence_in_file("test.txt", "four") == 0
    assert count_word_occurrence_in_file("test.txt", "o") == 0
    with pytest.raises(FileNotFoundError):
        assert count_word_occurrence_in_file("wrong.txt", "one")

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

def test_Pet():
    dog = Pet("cat")
    assert dog.name == "cat"
    assert dog.name != "dog"
    assert dog.hunger == 0
    dog.go_for_a_walk()
    assert dog.hunger == 1
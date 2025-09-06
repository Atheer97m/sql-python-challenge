import sqlite3
from queries import number_of_directors, list_of_directors, list_of_movies_about_river

def test_number_of_directors():
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    result = number_of_directors(db)
    conn.close()
    assert result == 4089

def test_list_of_directors():
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    result = list_of_directors(db)
    conn.close()
    assert "Aamir Khan" in result
    assert isinstance(result, list)

def test_list_of_movies_about_river():
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()
    result = list_of_movies_about_river(db)
    conn.close()
    assert "A River Runs Through It" in result
    assert isinstance(result, list)

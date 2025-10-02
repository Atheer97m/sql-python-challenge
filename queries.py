"""
Module for querying the movies database.
Contains functions to count directors, list directors, and find movies about rivers.
"""

def number_of_directors(db):
    """
    Return the total number of directors in the database.

    Parameters:
    db (sqlite3.Cursor): Database cursor.

    Returns:
    int: Number of directors.
    """
    query = "SELECT COUNT(*) FROM directors;"
    db.execute(query)
    result = db.fetchone()
    return result[0]


def list_of_directors(db):
    """
    Return a list of director names ordered alphabetically.

    Parameters:
    db (sqlite3.Cursor): Database cursor.

    Returns:
    list: Sorted list of director names.
    """
    query = "SELECT name FROM directors ORDER BY name ASC;"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]


def list_of_movies_about_river(db):
    """
    Return a list of movie titles that contain 'river' in the title.

    Parameters:
    db (sqlite3.Cursor): Database cursor.

    Returns:
    list: Sorted list of movie titles containing 'river'.
    """
    query = "SELECT title FROM movies WHERE LOWER(title) LIKE '%river%' ORDER BY title ASC;"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]


def number_of_directors_like(db, word):
    """
    Return the number of directors whose names contain a given word.

    Parameters:
    db (sqlite3.Cursor): Database cursor.
    word (str): Word to search for in director names.

    Returns:
    int: Count of matching directors.
    """
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?;"
    db.execute(query, [f"%{word}%"])
    result = db.fetchone()
    return result[0]


def list_of_movies_longer_than(db, min_length):
    """
    Return a list of movie titles longer than a given length in minutes.

    Parameters:
    db (sqlite3.Cursor): Database cursor.
    min_length (int): Minimum movie length in minutes.

    Returns:
    list: Sorted list of movie titles longer than min_length.
    """
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC;"
    db.execute(query, [min_length])
    results = db.fetchall()
    return [row[0] for row in results]

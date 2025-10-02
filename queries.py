"""
Queries for interacting with the movies.sqlite database.
Each function takes a `db` cursor connected to the database.
"""

def number_of_directors(db):
    """Return the total number of directors in the database."""
    query = "SELECT COUNT(*) FROM directors;"
    db.execute(query)
    result = db.fetchone()
    return result[0]


def list_of_directors(db):
    """Return a list of all director names sorted alphabetically."""
    query = "SELECT name FROM directors ORDER BY name ASC;"
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]


def list_of_movies_about_river(db):
    """Return a list of movies that contain the exact word 'river' in the title, sorted alphabetically."""
    query = """
        SELECT title
        FROM movies
        WHERE LOWER(title) LIKE '%river%'
        ORDER BY title ASC;
    """
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]


def number_of_directors_like(db, word):
    """Return the number of directors whose name contains the given word."""
    query = "SELECT COUNT(*) FROM directors WHERE name LIKE ?;"
    db.execute(query, [f"%{word}%"])
    result = db.fetchone()
    return result[0]


def list_of_movies_longer_than(db, min_length):
    """Return a list of movies longer than `min_length` minutes, sorted alphabetically."""
    query = "SELECT title FROM movies WHERE minutes > ? ORDER BY title ASC;"
    db.execute(query, [min_length])
    results = db.fetchall()
    return [row[0] for row in results]


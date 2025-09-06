def number_of_directors(db):
    query = """
    SELECT COUNT(*) FROM directors
    """
    db.execute(query)
    result = db.fetchone()
    return result[0]

def list_of_directors(db):
    query = """
    SELECT name FROM directors
    ORDER BY name ASC
    """
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]

def list_of_movies_about_river(db):
    query = """
    SELECT title FROM movies
    WHERE
      title LIKE '% river %' OR
      title LIKE 'river %' OR
      title LIKE '% river' OR
      title = 'river'
    ORDER BY title ASC
    """
    db.execute(query)
    results = db.fetchall()
    return [row[0] for row in results]

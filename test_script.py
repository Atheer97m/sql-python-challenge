import sqlite3
from queries import number_of_directors, list_of_directors, list_of_movies_about_river


def main():
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()

    print("Number of directors:", number_of_directors(db))
    print("List of directors (first 10):", list_of_directors(db)[:10])
    print("Movies with 'river' in the title:", list_of_movies_about_river(db))

    conn.close()


if __name__ == "__main__":
    main()

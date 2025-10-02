import sqlite3
from queries import (
    number_of_directors,
    list_of_directors,
    list_of_movies_about_river,
    number_of_directors_like,
    list_of_movies_longer_than
)

def main():
    # الاتصال بقاعدة البيانات
    conn = sqlite3.connect('data/movies.sqlite')
    db = conn.cursor()

    # تجربة كل الدوال
    print("Number of directors:", number_of_directors(db))
    print("First 10 directors:", list_of_directors(db)[:10])
    print("Movies with 'river' in the title:", list_of_movies_about_river(db))
    print("Number of directors with 'Smith' in name:", number_of_directors_like(db, 'Smith'))
    print("Movies longer than 120 minutes:", list_of_movies_longer_than(db, 120)[:10])

    # غلق الاتصال
    conn.close()


if __name__ == "__main__":
    main()

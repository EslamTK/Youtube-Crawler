import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS videos (
                  id integer PRIMARY KEY,
                  title text NOT NULL,
                  duration text NOT NULL,
                  views integer NOT NULL,
                  url text NOT NULL,
                  thumbnail_url text NOT NULL,
                  image_url text NOT NULL
                  )''')


def insert_videos_info(videos_info):
    cursor.executemany('''INSERT INTO videos (title, duration, views, url, thumbnail_url, image_url) 
                          VALUES (?, ?, ?, ?, ?, ?)''', videos_info)
    connection.commit()


def close_connection():
    if connection is not None:
        connection.close()

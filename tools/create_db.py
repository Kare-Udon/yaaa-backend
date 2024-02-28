import os
import click
import sqlite3


def create_table(db):
    # Connect to the database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    # Create the audio table
    c.execute('''CREATE TABLE IF NOT EXISTS audio
                 (id INTEGER PRIMARY KEY,
                 url VARCHAR(255),
                 is_ann INTEGER)''')
    
    # Create the tag table
    c.execute('''CREATE TABLE IF NOT EXISTS tag
                 (id INTEGER PRIMARY KEY,
                 name VARCHAR(255))''')
    
    # Create the annotation table
    c.execute('''CREATE TABLE IF NOT EXISTS annotation
                 (id INTEGER PRIMARY KEY,
                 audio_id INTEGER,
                 start INTEGER,
                 end INTEGER,
                 tag_id INTEGER,
                 FOREIGN KEY (audio_id) REFERENCES audio (id),
                 FOREIGN KEY (tag_id) REFERENCES tag (id))''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    
def insert_tag(db, name):
    # Connect to the database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    # Insert the tag into the tag table
    c.execute('INSERT INTO tag (name) VALUES (?)', (name,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    

def insert_audio(db, url):
    # Connect to the database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    # Insert the audio into the audio table
    c.execute('INSERT INTO audio (url, is_ann) VALUES (?, 0)', (url,))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    

@click.command()
@click.option('-d', '--db', default='./db.sqlite3', help='Sqlite3 database file')
@click.option('-a', '--audio', default="./audio", help='Audio file folder')
@click.option('-t', '--tag', help='Annotion tag, seperated by comma', required=True)
def create_db(db, audio, tag):
    create_table(db)
    
    # insert audio into database
    for root, _, files in os.walk(audio):
        for file in files:
            insert_audio(db, os.path.join(root, file))
    
    # insert tags into database
    for t in tag.split(','):
        insert_tag(db, t)

    
if __name__ == '__main__':
    create_db()

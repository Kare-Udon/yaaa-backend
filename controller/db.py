import sqlite3
import toml

from model.audio_data import Audio, Task, AnnotationGroup
from model.annotation_data import AnnotationData


audio_config = toml.load('config.toml')['audio']


def get_new_audio(id: int):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    # Get the song from the song table
    c.execute('SELECT * FROM song WHERE id = ?', (id,))
    audio = c.fetchone()
    if audio is None:
        return None
    while audio[2] == 1:
        id += 1
        c.execute('SELECT * FROM song WHERE id = ?', (id,))
        audio = c.fetchone()

    # Close the connection
    conn.close()

    # Create Audio object
    audio = Audio(id=audio[0], task=Task(
        feedback=audio_config["feedback"],
        visualization=audio_config["visualization"],
        annotationGroup=[AnnotationGroup(
            name="default", label=audio_config["tags"])],
        url=audio[1],
        alwaysShowTags=audio_config["always_show_tags"]
    ))

    return audio


def get_file_url(id: int):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    # Get the song from the song table
    c.execute('SELECT * FROM song WHERE id = ?', (id))
    audio = c.fetchone()

    # Close the connection
    conn.close()

    return audio[1]


def insert_annotation_data(data: AnnotationData):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    
    for annotation in data.annotations:
        # Get tag id
        c.execute('SELECT id FROM tag WHERE name = ?', (annotation.annotation,))
        id = c.fetchone()[0]
        
        # Insert annotiation data
        c.execute('INSERT INTO annotation (start, end, tag_id, song_id) VALUES (?, ?, ?, ?)',
                  (annotation.start, annotation.end, id, data.id))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

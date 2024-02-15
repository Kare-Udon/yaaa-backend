import sqlite3
import toml

from model.audio_data import Audio, Task, AnnotationGroup


audio_config = toml.load('config.toml')['audio']


def get_new_audio(id: int):
    # Connect to the database
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    # Get the song from the song table
    c.execute('SELECT * FROM song WHERE id = ?', (id + 1,))
    audio = c.fetchone()
    while audio[2] == 1:
        id += 1
        c.execute('SELECT * FROM song WHERE id = ?', (id + 1,))
        audio = c.fetchone()

    # Close the connection
    conn.close()

    # Create Audio object
    audio = Audio(id=audio[0], task=Task(
        feedback=audio_config["feedback"],
        visualization=audio_config["visualization"],
        annotationGroup=[AnnotationGroup(name="default", label=audio_config["tags"])],
        url=audio[1],
        alwaysShowTags=audio_config["always_show_tags"]
    ))

    return audio
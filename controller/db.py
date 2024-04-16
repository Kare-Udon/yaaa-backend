import sqlite3
import toml

from model.audio_data import Audio, Task, AnnotationGroup
from model.annotation_data import AnnotationData


audio_config = toml.load('config.toml')['audio']
db_config = toml.load('config.toml')['db']


def get_new_audio(id: int) -> Audio:
    """Get the audio from the database

    Args:
        id (int): The id of the audio

    Returns:
        Audio: The audio object
    """
    conn = sqlite3.connect(db_config["file"])
    c = conn.cursor()

    # Get the audio from the audio table
    c.execute('SELECT * FROM audio WHERE id=?', (id,))
    audio = c.fetchone()
    if audio is None:
        return None
    while audio[2] == 1:
        id += 1
        c.execute('SELECT * FROM audio WHERE id=?', (id,))
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


def get_file_url(id: int) -> str:
    """Get the file url from the database

    Args:
        id (int): The id of the audio

    Returns:
        str: The file url
    """
    conn = sqlite3.connect(db_config["file"])
    c = conn.cursor()

    # Get the audio from the audio table
    c.execute('SELECT * FROM audio WHERE id=?', (id,))
    audio = c.fetchone()

    # Close the connection
    conn.close()

    return audio[1]


def set_annotated(id: int):
    """Set the audio is_ann tag to True

    Args:
        id (int): The id of the audio
    """
    conn = sqlite3.connect(db_config["file"])
    c = conn.cursor()
    c.execute('UPDATE audio SET is_ann=1 WHERE id=?', (id,))
    conn.commit()
    conn.close()


def insert_annotation_data(data: AnnotationData):
    """Insert annotation data into the database

    Args:
        data (AnnotationData): Data to be inserted
    """
    conn = sqlite3.connect(db_config["file"])
    c = conn.cursor()

    for annotation in data.annotations:
        # Get tag id
        c.execute('SELECT id FROM tag WHERE name=?',
                  (annotation.annotation,))
        id = c.fetchone()[0]

        # Insert annotiation data
        c.execute('INSERT INTO annotation (start, end, tag_id, audio_id) VALUES (?, ?, ?, ?)',
                  (annotation.start, annotation.end, id, data.id,))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    # Set audio is_ann tag to True
    set_annotated(data.id)

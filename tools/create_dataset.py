import os
from pathlib import Path
import sqlite3
import uuid

import click
from pydub import AudioSegment


def get_tag_dict(db: str):
    conn = sqlite3.connect(db)

    c = conn.cursor()
    c.execute('SELECT id, name FROM tag')
    tag_list = c.fetchall()

    tag_dict = {}
    for tag in tag_list:
        tag_dict[tag[0]] = tag[1]

    conn.close()

    return tag_dict


def output_audio(db: str, output: str):
    conn = sqlite3.connect(db)

    c = conn.cursor()

    # get annotated audios
    c.execute('SELECT id, url FROM audio WHERE is_ann = 1')
    audios = c.fetchall()
    # turn into dict
    audio_set = {}
    for audio in audios:
        audio_set[audio[0]] = audio[1]

    # get annotations
    c.execute('SELECT audio_id, start, end, tag_id FROM annotation')
    annotations = c.fetchall()

    for anno in annotations:
        audio_id = anno[0]
        start = int(anno[1] * 1000)
        end = int(anno[2] * 1000)
        tag_id = anno[3]
        tag = get_tag_dict(db)[tag_id]
        audio = AudioSegment.from_file(audio_set[audio_id])
        audio = audio[start:end]
        # file name format: uuid-duration.wav
        audio.export(Path(output,
                          tag,
                          f"{str(uuid.uuid4()).split('-')[-1]}-{end - start}.wav"),
                     format="wav")

    print(f"Processed {len(annotations)} annotations.")


@click.command()
@click.option('-d', '--db', default='./db.sqlite3', help='Sqlite3 database file')
@click.option('-o', '--output', default="./dataset", help='Output folder')
def main(db: str, output: str):
    tags = get_tag_dict(db)
    # create output folders for tags
    for tag in tags.values():
        os.makedirs(Path(output, tag), exist_ok=True)

    # output audio
    output_audio(db, output)


if __name__ == '__main__':
    main()

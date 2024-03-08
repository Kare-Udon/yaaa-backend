import os
from pydub import AudioSegment
from pathlib import Path

import click


def cut_audio(path: Path, output: Path):
    audio = AudioSegment.from_file(path)

    # split into 30s segments, with 5s overlap
    interval = 30 * 1000
    overlap = 5 * 1000
    for i in range(0, len(audio), interval - overlap):
        audio[i:i+interval].export(output /
                                   f"{path.stem}_{i//1000}.wav", format="wav")


@click.command()
@click.option('-a', '--audio', default="./audio", help='Audio file folder')
@click.option('-o', '--output', default="./processed_audio", help='Output folder')
def main(audio: str, output: str):
    audio_folder = Path(audio)
    output_folder = Path(output)

    if not output_folder.exists():
        os.makedirs(output_folder)

    # output processing file number
    audio_files = list(audio_folder.glob("*.wav")) + \
        list(audio_folder.glob("*.mp3"))
    print(f"Processing {len(audio_files)} files")

    # read all audio files in the folder
    for audio_file in audio_files:
        # filter too short audio (2s)
        if len(AudioSegment.from_file(audio_file)) < 2 * 1000:
            continue
        cut_audio(audio_file, output_folder)


if __name__ == "__main__":
    main()

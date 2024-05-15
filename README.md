# YAAA - Backend

**A backend server for [YAAA](https://github.com/Kare-Udon/yaaa)**

English | [中文](README.zh.md)

## Description

YAAA-Backend is a backend server for YAAA, a simple and easy-to-use audio data annotator. It is built with [FastAPI](https://fastapi.tiangolo.com/) and [SQLite](https://www.sqlite.com/).

## Usage

### Install Dependencies

```bash
pip install -r requirements.txt
```

### (Optional) Preprocess Audio Data

If you have raw audio data (with long length) to be preprocessed, you can choose to use our `tools/preprocessing.py` script to do so.

We provide a base tool to split audio files into 10s chunks with 1s overlap, which is easier to annotate using YAAA.

Run the following command to split the audio files.

```bash
python tools/preprocessing.py [your args]

Options:
  -a, --audio TEXT   Audio file folder
  -o, --output TEXT  Output folder
  --help             Show this message and exit.
```

### Create Audio Database

Run the following command to create a database for audio data annotation work.

```bash
python tools/create_db.py

Options:
  -d, --db TEXT     Sqlite3 database file
  -a, --audio TEXT  Audio file folder
  -t, --tag TEXT    Annotion tag, seperated by comma  [required]
  --help            Show this message and exit.
```

**Hint: no space between tags and commas**

### Start Backend Server

Run the following command to start the backend server.

```bash
python main.py
```

The server will be hosted at `0.0.0.0:8000`.

## Generate Audio Dataset

You should install ffmpeg first.

[Install ffmpeg](https://ffmpeg.org/download.html)

Run the following command to generate dataset.

```bash
python tools/create_dataset.py

Options:
  -d, --db TEXT      Sqlite3 database file
  -o, --output TEXT  Output folder
  -n, --name TEXT    Output dataset name
  --help             Show this message and exit.
```

There will be a CSV file in the output folder. Use `pandas.read_csv` to read it as a `DataFrame`.

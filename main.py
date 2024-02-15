from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.audio_data import Audio
from model.annotation_data import AnnotationData
from controller.db import get_new_audio

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Yaaa Backend is running!"


@app.get("/audio")
async def get_audio(id: int):
    audio: Audio = get_new_audio(id)
    return audio


@app.post("/annotation")
async def post_annotation(data: AnnotationData):
    return data

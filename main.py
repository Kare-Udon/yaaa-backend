from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.audio_data import Audio
from model.annotation_data import AnnotationData

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
async def get_audio():
    audio: Audio = {
        "id": 1,
        "task": {
            "feedback": "none",
            "visualization": "spectrogram",
            "annotationGroup": [
                {
                    "name": "test",
                    "label": [
                        "test1",
                        "test2"
                    ]
                }
            ],
            "url": "/static/wav/spectrogram_demo_doorknock_mono.wav",
            "alwaysShowTags": True
        }
    }
    return audio


@app.post("/annotation")
async def post_annotation(data: AnnotationData):
    return data

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from model.audio_data import Audio
from model.annotation_data import AnnotationData
from controller.db import get_new_audio, get_file_url, insert_annotation_data

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
    if audio is None:
        raise HTTPException(status_code=400, detail="Audio not found")
    return audio


@app.post("/annotation")
async def post_annotation(data: AnnotationData):
    insert_annotation_data(data=data)
    return "200 OK"


@app.get("/file")
async def get_file(id: str):
    url = get_file_url(id)
    return FileResponse(url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

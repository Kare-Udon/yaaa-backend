from pydantic import BaseModel


class Annotation(BaseModel):
    id: str
    start: float
    end: float
    annotation: str


class AnnotationData(BaseModel):
    id: int
    task_start_time: int
    task_end_time: int
    annotations: list[Annotation]

from pydantic import BaseModel

class AnnotationData(BaseModel):
    class Annotation:
        id: str
        start: float
        end: float
        annotation: str
        
    id: int
    task_start_time: int
    task_start_end: int
    annotitions: list[Annotation]

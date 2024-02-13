from pydantic import BaseModel


class AnnotationGroup(BaseModel):
    name: str
    label: list[str]


class Task(BaseModel):
    feedback: str
    visualization: str
    annotationGroup: list[AnnotationGroup]
    url: str
    alwaysShowTags: bool


class Audio(BaseModel):
    id: int
    task: Task

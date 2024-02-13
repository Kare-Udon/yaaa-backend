from pydantic import BaseModel


class Aduio(BaseModel):
    class Task:
        class AnnotationGroup:
            name: str
            label: list[str]
        
        feedback: str
        visualization: str
        annotationGroup: list[AnnotationGroup]
        url: str
        alwaysShowTags: bool
    
    id: int
    task: Task

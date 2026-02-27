from typing import List, Optional
from pydantic import BaseModel, Field

class KnowledgeNode(BaseModel):
    title: str
    type: str  # section, group, series, page
    kind: Optional[str] = None # api-index, lom-object, js-class, etc
    slug: str
    filePath: Optional[str] = None
    sourceUrl: str
    description: str
    children: Optional[List["KnowledgeNode"]] = Field(default=None)

class KnowledgeMap(BaseModel):
    version: str = "1.0.0"
    nodes: List[KnowledgeNode] = Field(default_factory=list)

KnowledgeNode.model_rebuild()

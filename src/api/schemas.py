from pydantic import BaseModel, Field
from typing import List, Dict


class CVParseRequest(BaseModel):
    id: str
    cv_text: str


class JobParseRequest(BaseModel):
    id: str
    jd_text: str


class CVParseResponse(BaseModel):
    candidate_id: str
    skills: List[str] = Field(default_factory=list)
    years_experience_total: float = 0.0
    languages: List[Dict] = Field(default_factory=list)
    education: List[Dict] = Field(default_factory=list)
    experience: List[Dict] = Field(default_factory=list)
    cv_text: str


class JobParseResponse(BaseModel):
    job_id: str
    must_have: List[str] = Field(default_factory=list)
    nice_to_have: List[str] = Field(default_factory=list)
    seniority: str = "unspecified"
    lang_req: Dict = Field(default_factory=dict)
    jd_text: str

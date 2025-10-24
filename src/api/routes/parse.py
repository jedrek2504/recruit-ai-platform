from fastapi import APIRouter, HTTPException
from ..schemas import CVParseRequest, JobParseRequest, CVParseResponse, JobParseResponse
from ...parsing.cv_parser import CVParser
from ...parsing.job_parser import JobParser

parse = APIRouter(prefix="/parse", tags=["parse"])

cv_parser = CVParser()
job_parser = JobParser()


@parse.post("/cv", response_model=CVParseResponse)
def parse_cv(payload: CVParseRequest):
    if not payload.cv_text.strip():
        raise HTTPException(status_code=422, detail="cv_text is empty")
    result = cv_parser.parse(payload.id, payload.cv_text)
    return CVParseResponse(**result)  # ** -> dict unpacking


@parse.post("/job", response_model=JobParseResponse)
def parse_job(payload: JobParseRequest):
    if not payload.jd_text.strip():
        raise HTTPException(status_code=422, detail="jd_text is empty")
    result = job_parser.parse(payload.id, payload.jd_text)
    return JobParseResponse(**result)

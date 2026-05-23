from fastapi import APIRouter

from pydantic import BaseModel

from services.role_predictor import (
    predict_role
)

from services.ats_predictor import (
    predict_ats_score
)

from services.skill_extractor import (
    extract_skills
)

from services.job_matcher import (
    match_jobs
)

from services.recommendation_engine import (
    recommend_jobs
)

router = APIRouter(
    prefix="/predict",
    tags=["Resume Prediction"]
)

class ResumeRequest(BaseModel):

    resume_text: str

@router.post("/resume")

def analyze_resume(data: ResumeRequest):

    # INPUT TEXT
    resume_text = data.resume_text

    # ROLE PREDICTION
    role = predict_role(resume_text)

    # ATS SCORE
    ats_score = predict_ats_score(
        resume_text
    )

    # SKILLS
    skills = extract_skills(
        resume_text
    )

    # JOB MATCHING
    matched_jobs = match_jobs(
        resume_text
    )

    # JOB RECOMMENDATIONS
    recommendations = recommend_jobs(
        resume_text
    )

    return {

        "predicted_role": role,

        "ats_score": ats_score,

        "skills": skills,

        "matched_jobs": matched_jobs,

        "recommendations": recommendations
    }
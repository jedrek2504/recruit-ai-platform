from .skills import extract_skills


class CVParser:

    def parse(self, candidate_id: str, cv_text: str) -> dict:
        return {
            "candidate_id": candidate_id,
            "skills": extract_skills(cv_text),
            "years_experience_total": 0.0,
            "languages": [],
            "education": [],
            "experience": [],
            "cv_text": cv_text.strip(),
        }

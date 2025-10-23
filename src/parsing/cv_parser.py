class CVParser:

    def parse(self, candidate_id: str, cv_text: str) -> dict:
        return {
            "candidate_id": candidate_id,
            "skills": [],
            "years_experience_total": 0.0,
            "languages": [],
            "education": [],
            "experience": [],
            "cv_text": cv_text.strip(),
        }

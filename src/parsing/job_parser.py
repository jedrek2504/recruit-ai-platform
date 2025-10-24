from .skills import extract_skills


class JobParser:

    def parse(self, job_id: str, jd_text: str) -> dict:
        return {
            "job_id": job_id,
            "must_have": extract_skills(
                jd_text
            ),  # Extract all skills to must-have for now
            "nice_to_have": [],
            "seniority": "unspecified",
            "lang_req": {},
            "jd_text": jd_text.strip(),
        }

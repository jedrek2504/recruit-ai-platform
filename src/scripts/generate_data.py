import json
import random
from pathlib import Path

random.seed(42)
DATA = Path("data/raw")

SKILLS = ["python","pandas","numpy","scikit-learn","fastapi","pytest","docker","azure","sql","mlflow","nlp","git","linux"]

def make_candidate(i: int):
    skills = random.sample(SKILLS, k=random.randint(4,7))
    years = round(random.uniform(0.5,5.5),1)
    return {"id": f"C-{i:03d}", "cv_text": f"{years} years of experience. Skills: {', '.join(skills)}."}

def make_job(i: int):
    must = random.sample(SKILLS, k=3)
    return {"id": f"JD-{i:03d}", "jd_text": f"Looking for: {', '.join(must)}. Seniority: mid."}

def main():
    with open(DATA/"candidates.jsonl","w",encoding="utf-8") as f:
        for i in range(30):
            f.write(json.dumps(make_candidate(i+1), ensure_ascii=False)+"\n")
    with open(DATA/"jobs.jsonl","w",encoding="utf-8") as f:
        for i in range(3):
            f.write(json.dumps(make_job(i+1), ensure_ascii=False)+"\n")
    print("Generated data in data/raw/")

if __name__ == "__main__":
    main()
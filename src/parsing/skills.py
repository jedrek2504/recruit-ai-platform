from __future__ import annotations
import re
from typing import List

# 30 sample skills
SKILLS: List[str] = [
    "python",
    "pandas",
    "numpy",
    "fastapi",
    "pytest",
    "docker",
    "linux",
    "git",
    "sql",
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "kafka",
    "airflow",
    "azure",
    "aws",
    "gcp",
    "mlflow",
    "nlp",
    "opencv",
    "matplotlib",
    "seaborn",
    "xgboost",
    "lightgbm",
    "pytorch",
    "django",
    "flask",
]


def normalize_text(text: str) -> str:
    """Lowercase + whitespace normalization."""
    t = (text or "").lower()
    t = re.sub(r"\s+", " ", t).strip()
    return t


def _is_whole_word_present(t: str, token: str) -> bool:
    """Simple whole-word match using regex word boundaries."""
    pattern = r"\b" + re.escape(token) + r"\b"
    return re.search(pattern, t) is not None


def dedupe_preserve_order(items: List[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for s in items:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def extract_skills(raw_text: str) -> List[str]:
    """Extract canonical skills based on word matches."""
    t = normalize_text(raw_text)
    found: List[str] = []
    for skill in SKILLS:
        if _is_whole_word_present(t, skill):
            found.append(skill)
    return dedupe_preserve_order(found)

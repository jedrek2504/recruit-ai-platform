import pytest
from parsing.skills import extract_skills, normalize_text, SKILLS


def test_basic_three_skills():
    text = "Python, Pandas, Linux"
    out = extract_skills(text)
    assert out == ["python", "pandas", "linux"]


def test_case_insensitive_and_whitespace():
    text = "  PYTHON   \n pandas\t,   LiNuX  "
    out = extract_skills(text)
    assert out == ["python", "pandas", "linux"]


def test_whole_word_boundaries_no_false_positives():
    text = "I like pythonic code and fastapi-like frameworks."
    out = extract_skills(text)
    # shouldn't match 'pythonic' nor 'fastapi-like' as whole words
    assert "python" not in out
    assert "fastapi" not in out


def test_dedup_and_order_preserved():
    text = "python and pandas, then python again, and finally linux then pandas"
    out = extract_skills(text)
    # first appearances define order; duplicates are removed
    assert out == ["python", "pandas", "linux"]


@pytest.mark.parametrize(
    "text,expected",
    [
        ("We use SQL and PostgreSQL plus Redis", ["sql", "postgresql", "redis"]),
        (
            "Scikit learn (spelled without hyphen) should NOT match now",
            [],
        ),  # not in vocab
        ("Kafka with Airflow and AWS", ["kafka", "airflow", "aws"]),
    ],
)
def test_various_vocab_combinations(text, expected):
    out = extract_skills(text)
    assert out == expected


def test_no_skills_returns_empty_list():
    text = "We value communication and teamwork."
    out = extract_skills(text)
    assert out == []


def test_normalize_text_helpers():
    # sanity check for normalize_text behavior
    raw = "  PyThOn   \n  PaNdAs  "
    norm = normalize_text(raw)
    assert norm == "python pandas"
    # and extract should pick both
    out = extract_skills(raw)
    assert out == ["python", "pandas"]


def test_vocab_is_lowercase_and_without_specials():
    # ensure current canonical vocab follows the agreed simple rules
    assert all(s == s.lower() for s in SKILLS)
    assert all("/" not in s and "+" not in s for s in SKILLS)

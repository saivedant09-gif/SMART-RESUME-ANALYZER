import re

def calculate_jd_match(resume_text, job_description):

    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    jd_words = set(re.findall(r'\w+', job_description.lower()))

    matched = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0, []

    score = int((len(matched) / len(jd_words)) * 100)

    return score, sorted(matched)
import json

with open("data/job_roles.json", "r") as file:
    JOB_ROLES = json.load(file)


def analyze_resume(role, detected_skills):

    required_skills = JOB_ROLES[role]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in detected_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)

    return score, matched, missing
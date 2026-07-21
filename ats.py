import re

def calculate_ats_score(resume_text, skills):

    score = 0
    feedback = []

    text = resume_text.lower()

    # Contact Information (5)
    if re.search(r'[\w\.-]+@[\w\.-]+', text):
        score += 5
    else:
        feedback.append("Add a professional email address.")

    # Phone Number (5)
    if re.search(r'\d{10}', text):
        score += 5
    else:
        feedback.append("Add a phone number.")

    # Education (15)
    if "education" in text:
        score += 15
    else:
        feedback.append("Include an Education section.")

    # Projects (15)
    if "project" in text:
        score += 15
    else:
        feedback.append("Add project experience.")

    # Experience (25)
    if "experience" in text or "internship" in text:
        score += 25
    else:
        feedback.append("Include internships or work experience.")

    # Certifications (10)
    if "certification" in text or "certifications" in text:
        score += 10
    else:
        feedback.append("Add certifications.")

    # Skills (25)
    skill_score = min(len(skills) * 2.5, 25)
    score += skill_score

    score = round(score)

    return score, feedback
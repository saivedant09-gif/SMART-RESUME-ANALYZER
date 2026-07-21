from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, score, match_score, skills, matched_skills, missing_skills, feedback):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Title"]))

    elements.append(Paragraph(f"ATS Score: {score}%", styles["BodyText"]))
    elements.append(Paragraph(f"Job Match: {match_score}%", styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Detected Skills</b>", styles["Heading2"]))
    for skill in skills:
        elements.append(Paragraph(skill, styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Matching Skills</b>", styles["Heading2"]))
    for skill in matched_skills:
        elements.append(Paragraph(skill, styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing_skills:
        elements.append(Paragraph(skill, styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Suggestions</b>", styles["Heading2"]))
    for item in feedback:
        elements.append(Paragraph(item, styles["BodyText"]))

    doc.build(elements)
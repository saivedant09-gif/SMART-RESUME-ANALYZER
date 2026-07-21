import re

def highlight_keywords(text, skills):

    highlighted = text

    for skill in skills:
        pattern = re.compile(re.escape(skill), re.IGNORECASE)
        highlighted = pattern.sub(
            f"<mark>{skill}</mark>",
            highlighted
        )

    return highlighted
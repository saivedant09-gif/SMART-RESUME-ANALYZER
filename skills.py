SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "MySQL",
    "SQLite",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "AWS",
    "Azure",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Flask",
    "Django",
    "Streamlit",
    "Linux"
]

def extract_skills(resume_text):
    detected_skills = []

    resume_text = resume_text.lower()

    for skill in SKILLS:
        if skill.lower() in resume_text:
            detected_skills.append(skill)

    return sorted(set(detected_skills))


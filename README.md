<div align="center">

# 📄 Smart Resume Analyzer

### Analyze • Match • Improve Your Resume 

Streamlit app link: https://smart-resume-analyzer-saivedant09.streamlit.app/

An intelligent Resume Analyzer built using **Python**, **Streamlit**, and **NLP techniques** that evaluates resumes, calculates an ATS score, matches resumes with job roles, compares them against job descriptions, and generates a professional PDF report.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📌 Overview

Recruiters often use **Applicant Tracking Systems (ATS)** to filter resumes before they reach hiring managers.

This project helps job seekers analyze their resumes by:

- Calculating an ATS Score
- Detecting technical skills
- Matching resumes with selected job roles
- Comparing resumes with job descriptions
- Suggesting improvements
- Generating downloadable PDF reports

---

# ✨ Features

## 📄 Resume Upload

- Upload PDF Resume
- Upload DOCX Resume

---

## 🛠 Resume Parsing

- Extract text from PDF
- Extract text from DOCX

---

## 📊 ATS Score

- Resume scoring
- Resume rating
- Improvement suggestions

---

## 🎯 Job Role Matching

Supports multiple roles including:

- Data Scientist
- AI Engineer
- Python Developer
- Full Stack Developer
- Data Analyst

Shows:

- Job Match Percentage
- Matching Skills
- Missing Skills

---

## 📋 Job Description Matching

Paste any Job Description to:

- Compare with resume
- Calculate JD Match %
- Find matching keywords

---

## 📈 Data Visualization

Interactive charts using Plotly:

- Pie Chart
- Bar Chart

---

## 📄 PDF Report

Generate and download a professional Resume Analysis Report including:

- ATS Score
- Job Match
- Skills
- Missing Skills
- Suggestions

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| Charts | Plotly |
| PDF Parsing | PyMuPDF |
| DOCX Parsing | python-docx |
| Data Handling | Pandas |
| PDF Report | ReportLab |

---

# 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── parser.py
├── skills.py
├── ats.py
├── analyzer.py
├── jd_match.py
├── report.py
├── highlighter.py
│
├── data/
│   └── job_roles.json
│
├── uploads/
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
```

### Move into Project

```bash
cd AI-Resume-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---


# 🧠 Workflow

```text
Upload Resume
       │
       ▼
Extract Resume Text
       │
       ▼
Detect Skills
       │
       ▼
Calculate ATS Score
       │
       ▼
Job Role Matching
       │
       ▼
Job Description Matching
       │
       ▼
Generate Suggestions
       │
       ▼
Visual Analytics
       │
       ▼
Download PDF Report
```

---

# 📊 Future Improvements

- AI-powered resume suggestions using LLMs
- Automatic resume summarization
- Multiple resume comparison
- Resume ranking
- LinkedIn profile analysis
- Cloud deployment
- Authentication system

---

# 👨‍💻 Author

## R Sai Vedant

Computer Science (Data Science) Student

VIT Vellore

- 💻 Python Developer
- 🤖 AI Enthusiast
- 📊 Data Science Learner
- 🌐 Full Stack Learner

---

# ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.

It motivates future development and helps others discover the project.

---

## 📜 License

This project is licensed under the MIT License.

---

<div align="center">

Made with ❤️ using Python & Streamlit

</div>

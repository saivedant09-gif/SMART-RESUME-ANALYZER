import streamlit as st
import os
import plotly.express as px
import pandas as pd
from report import generate_report
from parser import extract_pdf_text, extract_docx_text
from skills import extract_skills
from ats import calculate_ats_score
from analyzer import analyze_resume
from jd_match import calculate_jd_match
from highlighter import highlight_keywords

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and analyze it using AI.")

uploaded_file = st.file_uploader(
    "Choose your Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
        st.success("Resume Uploaded Successfully!")

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

            if uploaded_file.name.endswith(".pdf"):
                resume_text = extract_pdf_text(file_path)

            else:
                resume_text = extract_docx_text(file_path)
        
        skills = extract_skills(resume_text)
        score, feedback = calculate_ats_score(
            resume_text,
            skills
        )

        if score >= 90:
            rating = "🌟 Excellent"

        elif score >= 75:
            rating = "✅ Good"

        elif score >= 60:
            rating = "🟡 Average"

        else:
            rating = "🔴 Needs Improvement"

        st.subheader("Resume Rating")

        st.info(rating)

        highlighted_resume = highlight_keywords(
        resume_text,
        skills
        )
        word_count = len(resume_text.split())
        line_count = len(resume_text.splitlines())
        character_count = len(resume_text)

        st.subheader("📈 Resume Statistics")

        c1, c2, c3 = st.columns(3)

        c1.metric("Words", word_count)
        c2.metric("Lines", line_count)
        c3.metric("Characters", character_count)
        with st.expander("📄 Resume with Highlighted Keywords"):
            st.markdown(
                highlighted_resume,
                unsafe_allow_html=True
            )

        st.subheader("📋 Job Description")

        job_description = st.text_area(
            "Paste the Job Description Here",
            height=250,
            placeholder="Paste the company's job description..."
        )

        job_role = st.selectbox(
            "Select Job Role",
            [
                "Data Scientist",
                "AI Engineer",
                "Python Developer",
                "Full Stack Developer",
                "Data Analyst"
            ]
        )
        match_score, matched_skills, missing_skills = analyze_resume(
            job_role,
            skills
        )
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📊 ATS Score",
                f"{score}%"
            )

        with col2:
            st.metric(
                "🎯 Job Match",
                f"{match_score}%"
            )

        with col3:
            st.metric(
                "🛠 Skills",
                len(skills)
            )

        st.subheader("ATS Score")
        st.progress(score / 100)
        
        

        st.subheader("Job Match")
        st.progress(match_score / 100)

        
        st.subheader("🛠 Skills Detected")

        cols = st.columns(4)

        for i, skill in enumerate(skills):
            cols[i % 4].success(skill)

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matching Skills")

            for skill in matched_skills:
                st.success(skill)

        with right:

            st.subheader("❌ Missing Skills")

            for skill in missing_skills:
                st.error(skill)
        st.subheader("📊 Skill Analysis")

        chart_data = pd.DataFrame({
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        })

        fig = px.pie(
            chart_data,
            values="Count",
            names="Category",
            title="Matched vs Missing Skills"
        )

        st.plotly_chart(fig, use_container_width=True)
        comparison = pd.DataFrame({
            "Metric": ["ATS Score", "Job Match"],
            "Score": [score, match_score]
        })

        fig2 = px.bar(
            comparison,
            x="Metric",
            y="Score",
            title="ATS Score vs Job Match",
            text="Score"
        )

        st.plotly_chart(fig2, use_container_width=True)
        

        
        jd_score = 0
        matched_keywords = []

        if job_description.strip():

            jd_score, matched_keywords = calculate_jd_match(
                resume_text,
                job_description
            )
        
        st.subheader("Job Description Match")
        st.metric(
        "📋 JD Match",
        f"{jd_score}%"
        )
        st.progress(jd_score / 100)

        st.subheader("✅ Keywords Found")

        for word in matched_keywords:
            st.success(word)
        
        st.subheader("💡 Suggestions")

        for item in feedback:
            st.warning(item)

        generate_report(
        "Resume_Report.pdf",
        score,
        match_score,
        skills,
        matched_skills,
        missing_skills,
        feedback
        )
        with open("Resume_Report.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Resume Report",
                data=pdf_file,
                file_name="Resume_Report.pdf",
                mime="application/pdf"
            )
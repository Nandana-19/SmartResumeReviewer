import os
import streamlit as st
from resume_parser import extract_text
from llm_review import review_resume
from fpdf import FPDF

# --- Streamlit config ---
st.set_page_config(page_title="Smart Resume Reviewer", page_icon="📊", layout="wide")
st.title("📊 Smart Resume Reviewer Pro")
st.write("Upload or paste your resume, enter a target job role, and get AI-powered feedback!")

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Main container padding */
        .main .block-container { padding: 2rem 3rem; }

        /* Center title and color */
        h1, .stTitle { text-align: center; color: #2E86AB; }

        /* Tabs styling */
        .stTabs [role="tab"] { font-weight: bold; color: #2E86AB; }
        .stTabs [role="tab"]:hover { color: #F26419; }

        /* Text areas and feedback boxes */
        .resume-box, .feedback-box { background-color: #F8F9FA; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
        .resume-box pre, .feedback-box pre { max-height: 300px; overflow-y: auto; }

        /* Button styling */
        div.stButton > button:first-child {
            background-color: #2E86AB; color: white; font-size: 16px; height: 45px; width: 250px; border-radius: 8px;
        }
        div.stButton > button:first-child:hover { background-color: #F26419; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- Tabs ---
tab1, tab2 = st.tabs(["📄 Upload / Paste & Review", "📥 Download PDF Report"])

with tab1:
    # Upload or paste
    uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
    resume_text_area = st.text_area("Or paste your resume text here")
    job_role = st.text_input("Enter the target job role")

    if st.button("🔍 Review Resume"):
        if (uploaded_file or resume_text_area.strip()) and job_role.strip():
            with st.spinner("Analyzing your resume... ⏳"):
                # Extract text from uploaded file
                if uploaded_file:
                    filename = uploaded_file.name
                    temp_path = os.path.join("temp_" + filename)
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    resume_text = extract_text(temp_path)
                else:
                    # Use pasted text
                    resume_text = extract_text(resume_text_area)

                # Call AI for feedback
                feedback = review_resume(resume_text, job_role)

                # Save results to session
                st.session_state["resume_text"] = resume_text
                st.session_state["feedback"] = feedback

            st.success("✅ Review Complete!")
            st.subheader("Resume Text Preview")
            st.text(resume_text[:500] + ("..." if len(resume_text) > 500 else ""))
            st.subheader("AI Feedback")
            st.write(feedback)
        else:
            st.error("⚠ Please provide a resume (upload or paste) and enter a job role.")

with tab2:
    st.subheader("Download Report as PDF")
    if "feedback" in st.session_state and "resume_text" in st.session_state:
        pdf_output_path = "resume_feedback.pdf"
        pdf = FPDF()
        pdf.add_page()
        # Use UTF-8 compatible font (make sure DejaVuSans.ttf is in your project folder)
        font_path = os.path.join(os.getcwd(), "DejaVuSans.ttf")
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", "", 12)

        pdf.multi_cell(0, 8, "Resume Text Preview:\n" + st.session_state["resume_text"][:1000] +
                       ("..." if len(st.session_state["resume_text"]) > 1000 else ""))
        pdf.ln(5)
        pdf.multi_cell(0, 8, "AI Feedback:\n" + st.session_state["feedback"])

        pdf.output(pdf_output_path)

        with open(pdf_output_path, "rb") as f:
            st.download_button(
                label="📥 Download Feedback as PDF",
                data=f,
                file_name="resume_feedback.pdf",
                mime="application/pdf"
            )
    else:
        st.info("Run the analysis in the first tab to generate the PDF report.")

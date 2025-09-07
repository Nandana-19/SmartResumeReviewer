
📊 Smart Resume Reviewer Pro

A web application that uses AI to review resumes, provide tailored feedback, and help job seekers optimize their resumes for specific roles.

---

## 📝 Problem Statement

Job seekers often struggle to tailor their resumes to match specific job roles. Recruiters spend only a few seconds scanning each resume, making it crucial for resumes to highlight relevant skills, experience, and keywords. This project aims to automate resume reviews and provide actionable AI-driven feedback to improve chances of landing interviews.

---

## ✨ Features

- Upload or paste a resume (PDF/TXT) for review.
- Enter a target job role to get role-specific feedback.
- Optionally provide a job description for enhanced feedback.
- AI-powered suggestions on:
  - Missing skills or keywords
  - Formatting and clarity improvements
  - Redundant or vague language
  - Tailoring experience to the role
- Preview resume and feedback within the app.
- Download reviewed resume and AI feedback as a PDF.
- Supports UTF-8 text and multiple languages.
- Clean, modern UI with tabs for review and downloads.

---

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Nandana-19/SmartResumeReviewer.git
cd SmartResumeReviewer
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run app.py
Open your browser and go to:

arduino
Copy code
http://localhost:8501
📦 Dependencies
Python 3.10+

streamlit

fpdf2

nltk

pdfplumber

openai

(Exact versions are listed in requirements.txt.)

🖼 Sample Usage / Screenshots
Upload or Paste Resume Tab:


AI Feedback Preview:


Download PDF Report:


💻 Commit and Push Changes
bash
Copy code
git add .
git commit -m "Final submission version"
git push origin main
⚠️ Notes
Ensure your OpenAI API key is set as an environment variable (OPENAI_API_KEY) before running the app.

Uploaded resumes are not stored to protect privacy.

AI feedback is for guidance only.

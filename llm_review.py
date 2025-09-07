from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_resume(resume_text, job_role, job_description=""):
    """
    Review a resume for a given job role, optionally using a job description.
    Args:
        resume_text (str): Text extracted from the resume.
        job_role (str): Target job role.
        job_description (str, optional): Job description for tailored feedback.
    Returns:
        str: Structured AI feedback.
    """
    prompt = f"""
    You are a career coach. Review this resume for the role of {job_role}.
    {f'Job Description: {job_description}' if job_description else ''}
    Resume:
    {resume_text}
    
    Provide:
    1. Missing skills/keywords
    2. Formatting/clarity suggestions
    3. Redundant or vague language
    4. Suggestions to tailor experience to the role
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


# ----------------- TEST RUNNER -----------------
if __name__ == "__main__":
    from resume_parser import extract_text

    # Sample resume file
    resume_text = extract_text(
        r"C:/Users/npadm/Documents/resume_text_extractor/test_files/resume_juanjosecarin.pdf"
    )

    # Example usage with job role and optional job description
    job_role = "Data Scientist"
    job_description = "Experience in machine learning, Python, data analysis, and model deployment."
    feedback = review_resume(resume_text, job_role, job_description)

    print("\n--- GPT-4 Feedback ---\n")
    print(feedback)

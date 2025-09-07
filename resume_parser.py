# -------------------- IMPORTS --------------------
import pdfplumber
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')

# -------------------- FUNCTIONS --------------------
def extract_text(file_path_or_text):
    """
    Extracts and cleans text from PDF, TXT resumes, plain text, or Streamlit UploadedFile.
    
    Args:
        file_path_or_text (str or UploadedFile): Path to the resume file, plain text, or Streamlit UploadedFile.
    
    Returns:
        str: Cleaned text from the resume.
    """
    try:
        text = ""

        # Case 1: Streamlit UploadedFile
        if hasattr(file_path_or_text, "read") and file_path_or_text.name.lower().endswith(".pdf"):
            with pdfplumber.open(file_path_or_text) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        # Case 2: PDF file path
        elif isinstance(file_path_or_text, str) and file_path_or_text.lower().endswith(".pdf"):
            with pdfplumber.open(file_path_or_text) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        # Case 3: TXT file path
        elif isinstance(file_path_or_text, str) and file_path_or_text.lower().endswith(".txt"):
            with open(file_path_or_text, "r", encoding="utf-8") as f:
                text = f.read()

        # Case 4: Already plain text
        elif isinstance(file_path_or_text, str):
            text = file_path_or_text

        else:
            print(f"Unsupported input type: {type(file_path_or_text)}")
            return ""

        # Clean text
        text = clean_text(text)
        return text.strip()

    except Exception as e:
        print(f"Error reading file {file_path_or_text}: {e}")
        return ""


def clean_text(text):
    """
    Cleans extracted text: removes extra spaces, empty lines, and special characters.
    """
    # Collapse multiple newlines
    text = re.sub(r'\n+', '\n', text)
    # Replace multiple spaces/tabs with one space
    text = re.sub(r'[ \t]+', ' ', text)
    # Strip leading/trailing spaces per line and remove empty lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return "\n".join(lines)


def summarize_keywords(text, top_n=10):
    """
    Returns the most frequent words (keywords) in the resume text, excluding stopwords.
    
    Args:
        text (str): Resume text.
        top_n (int): Number of top keywords to return.
    
    Returns:
        List of top keywords.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w not in stop_words]
    word_counts = Counter(filtered)
    return [word for word, count in word_counts.most_common(top_n)]


# -------------------- TEST RUNNER --------------------
if __name__ == "__main__":
    # Replace with your own resume file path
    sample_file = r"C:/Users/npadm/Documents/resume_text_extractor/test_files/resume_juanjosecarin.pdf"
    extracted = extract_text(sample_file)

    print("\n--- Extracted Text ---\n")
    print(extracted[:1000])  # Show first 1000 characters

    keywords = summarize_keywords(extracted)
    print("\n--- Top Keywords ---\n")
    print(keywords)


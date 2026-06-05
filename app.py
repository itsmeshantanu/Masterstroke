import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_resume_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text

resume_text = extract_resume_text("resume.pdf")

with open("jd.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

prompt = f"""
You are an ATS Resume Screening System.

Compare the resume with the job description.

Return in the following format:

Match Score: XX%

Matching Skills:
- skill1
- skill2

Missing Skills:
- skill1
- skill2

Recommendation:
Good Fit / Moderate Fit / Poor Fit

Job Description:
{jd_text}

Resume:
{resume_text}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n===== ATS RESULT =====\n")
print(response.choices[0].message.content)
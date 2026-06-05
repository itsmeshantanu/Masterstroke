# ATS Resume Matcher

## About

This project compares a candidate's resume with a job description and provides:

* Match Score
* Matching Skills
* Missing Skills
* Recommendation

The resume is read from a PDF file and the job description is read from a text file. Both are sent to an LLM through the Groq API, which analyzes the content and generates the result.

## Technologies Used

* Python
* Groq API
* PyPDF2
* python-dotenv

## Project Structure

```text
Master_stroke/
│
├── app.py
├── jd.txt
├── resume.pdf
├── .env
└── README.md
```

## How It Works

1. Extract text from the resume PDF.
2. Read the job description from a text file.
3. Create a prompt containing both resume and JD.
4. Send the prompt to the LLM.
5. Receive analysis from the model.
6. Display match score, skills, and recommendation.

## Installation

Install required packages:

```bash
pip install groq
pip install PyPDF2
pip install python-dotenv
```

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key
```

Run the project:

```bash
python app.py
```

## Sample Output

```text
Match Score: 80%

Matching Skills:
- Python
- SQL
- Pandas

Missing Skills:
- Machine Learning

Recommendation:
Good Fit
```

## Future Improvements

* Upload resumes through a web interface
* Support multiple resume formats
* Store results in a database
* Compare multiple candidates against a single job description

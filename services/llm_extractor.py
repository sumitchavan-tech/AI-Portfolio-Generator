import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_resume_data(resume_text):

    prompt = f"""
You are an expert resume parser and career advisor.

Extract information from the resume and return ONLY valid JSON.

Do not return explanations.
Do not return markdown.
Do not return code blocks.

Return JSON in exactly this structure:

{{
    "name": "",
    "email": "",
    "phone": "",
    "summary": "",
    "resume_score": "",

    "github": "",
    "linkedin": "",
    "portfolio": "",

    "skills": [],

    "career_recommendations": [],

    "skill_gaps": [],

    "strengths": [],

    "learning_recommendations": [],

    "projects": [
        {{
            "name": "",
            "description": ""
        }}
    ],

    "education": [
        {{
            "institution": "",
            "degree": "",
            "duration": ""
        }}
    ],

    "experience": [
        {{
            "role": "",
            "company": "",
            "duration": "",
            "responsibilities": []
        }}
    ]
}}

Rules:

1. Generate a professional 3-4 line summary.
2. Extract all technical skills.
3. Extract all projects.
4. Extract all education details.
5. Extract all internships/work experience.
6. Give a resume score between 0 and 100.
7. Recommend 3-5 career paths based on education, projects and skills.
8. Recommend 3-5 skills that the candidate should learn next.
9. Identify 3-5 strengths from the candidate's resume.
10. Provide 3-5 learning recommendations.
11. Extract GitHub URL if available.
12. Extract LinkedIn URL if available.
13. Extract portfolio website URL if available.
14. If GitHub URL is not present, return "".
15. If LinkedIn URL is not present, return "".
16. If Portfolio URL is not present, return "".
17. Never create, guess, or invent URLs.
18. Return ONLY valid JSON.
19. No markdown formatting.
20. No ```json blocks.

Resume Content:

{resume_text}
"""

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content
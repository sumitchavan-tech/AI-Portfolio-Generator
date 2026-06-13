from pydantic import BaseModel
from typing import List


class Education(BaseModel):
    institution: str = ""
    degree: str = ""
    duration: str = ""


class Project(BaseModel):
    name: str = ""
    description: str = ""


class Experience(BaseModel):
    role: str = ""
    company: str = ""
    duration: str = ""
    responsibilities: List[str] = []


class ResumeData(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""

    summary: str = ""

    resume_score: str = ""

    github: str = ""
    linkedin: str = ""
    portfolio: str = ""

    skills: List[str] = []

    career_recommendations: List[str] = []

    skill_gaps: List[str] = []

    strengths: List[str] = []

    learning_recommendations: List[str] = []

    projects: List[Project] = []

    education: List[Education] = []

    experience: List[Experience] = []
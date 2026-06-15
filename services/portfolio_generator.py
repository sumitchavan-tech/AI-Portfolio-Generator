import json

from jinja2 import Environment, FileSystemLoader
from pydantic import ValidationError

from services.models import ResumeData
from services.pdf_generator import generate_pdf


def generate_portfolio(
    ai_data,
    resume_filename,
    photo_filename
):

    ai_data = ai_data.replace(
        "```json",
        ""
    )

    ai_data = ai_data.replace(
        "```",
        ""
    )

    ai_data = ai_data.strip()

    try:

        json_data = json.loads(
            ai_data
        )

        resume = ResumeData(
            **json_data
        )

    except json.JSONDecodeError:

        raise Exception(
            "AI returned invalid JSON"
        )

    except ValidationError as e:

        raise Exception(
            f"Pydantic Validation Failed: {e}"
        )

    env = Environment(
        loader=FileSystemLoader(
            "templates"
        )
    )

    template = env.get_template(
        "portfolio_template.html"
    )

    output = template.render(

        name=resume.name,

        email=resume.email,

        phone=resume.phone,

        summary=resume.summary,

        resume_score=resume.resume_score,

        github=resume.github,

        linkedin=resume.linkedin,

        portfolio=resume.portfolio,

        skills=resume.skills,

        career_recommendations=resume.career_recommendations,

        skill_gaps=resume.skill_gaps,

        strengths=resume.strengths,

        learning_recommendations=resume.learning_recommendations,

        projects=resume.projects,

        education=resume.education,

        experience=resume.experience,

        resume_filename=resume_filename,

        photo_filename=photo_filename

    )

    safe_name = (
        resume.name
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )

    output_path = (
        f"generated_portfolios/{safe_name}.html"
    )

    with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:

     file.write(output)

    generate_pdf(
    resume,
    safe_name
)
    return output_path
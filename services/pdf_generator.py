from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(resume, output_name):

    os.makedirs("generated_pdfs", exist_ok=True)

    pdf_path = f"generated_pdfs/{output_name}.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"<b>{resume.name}</b>",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Email: {resume.email}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Phone: {resume.phone}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Professional Summary</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            resume.summary,
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>Resume Score:</b> {resume.resume_score}/100",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in resume.skills:
        content.append(
            Paragraph(
                f"- {skill}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Projects</b>",
            styles["Heading2"]
        )
    )

    for project in resume.projects:

        content.append(
            Paragraph(
                f"<b>{project.name}</b>",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                project.description,
                styles["Normal"]
            )
        )

    doc.build(content)

    return pdf_path
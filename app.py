from flask import Flask, render_template, request, send_from_directory
import os

from services.pdf_extractor import extract_text_from_pdf
from services.llm_extractor import extract_resume_data
from services.portfolio_generator import generate_portfolio
from services.link_extractor import extract_links

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PHOTO_FOLDER = "photos"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PHOTO_FOLDER"] = PHOTO_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PHOTO_FOLDER, exist_ok=True)
os.makedirs("generated_portfolios", exist_ok=True)
os.makedirs("generated_pdfs", exist_ok=True)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/portfolio/<filename>')
def open_portfolio(filename):
    return send_from_directory(
        "generated_portfolios",
        filename
) 

@app.route('/photos/<filename>')
def serve_photo(filename):
    return send_from_directory(
        "photos",
        filename
    )

@app.route('/pdf/<filename>')
def download_pdf(filename):
    return send_from_directory(
        "generated_pdfs",
        filename,
        as_attachment=True
)

@app.route('/upload', methods=['POST'])
def upload_resume():

    try:

        if 'resume' not in request.files:
            return """
            <h1>Error</h1>
            <p>No resume uploaded.</p>
            """

        file = request.files['resume']

        if file.filename == '':
            return """
            <h1>Error</h1>
            <p>Please select a resume PDF.</p>
            """

        file_path = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(file_path)

        resume_filename = file.filename

        photo_filename = None

        if 'photo' in request.files:

            photo = request.files['photo']

            if photo.filename != '':

                photo_path = os.path.join(
                    app.config['PHOTO_FOLDER'],
                    photo.filename
                )

                photo.save(photo_path)

                photo_filename = photo.filename

        resume_text = extract_text_from_pdf(
            file_path
        )

        links = extract_links(
            resume_text
        )

        ai_data = extract_resume_data(
            resume_text
        )

        print("\n===== EXTRACTED LINKS =====")
        print(links)

        print("\n===== AI RESPONSE =====")
        print(ai_data)
        print("=======================\n")

        portfolio_path = generate_portfolio(
            ai_data,
            resume_filename,
            photo_filename
        )

        portfolio_file = os.path.basename(
            portfolio_path
        )

        return f"""
        <h1>Portfolio Generated Successfully!</h1>

        <p>Portfolio saved successfully.</p>

        <br>

        <a href="/portfolio/{portfolio_file}">
            Open Portfolio
        </a>
        """

    except Exception as e:

        print("ERROR:", e)

        return f"""
        <h1>Something Went Wrong</h1>

        <p>{str(e)}</p>
        """

if __name__ == "__main__":
    app.run(debug=True)
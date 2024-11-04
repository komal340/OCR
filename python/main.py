from ai_engine import extract_text_from_image, summarize_text
from file_utils import save_file_to_upload, validate_file_from_request
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


# this is the default homepage when you enter localhost:5000 on browser
# The upload form page
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    # request object is sent after submitting the form and it contains image
    file = validate_file_from_request(request)

    if file is None:
        return redirect("/")

    image_path = save_file_to_upload(file)
    print(f"Image saved at: {image_path}")

    extracted_text = extract_text_from_image(image_path)
    summary = summarize_text(extracted_text)

    # Pass the extracted text and summary to the result.html template
    return render_template(
        "result.html", text_in_image=extracted_text, text_summary=summary
    )


# this if statement runs when we enter python main.py
if __name__ == "__main__":
    # starts the server on the default port(5000), visit localhost:5000
    # server is responsible for accepting request and giving response
    app.run(debug=True)

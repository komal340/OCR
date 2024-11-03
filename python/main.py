import os

import cv2
import pytesseract
from flask import Flask, redirect, render_template, request
from PIL import Image
from transformers import pipeline

app = Flask(__name__)

# Load the text summarization pipeline from transformers
summarizer = pipeline("summarization")


@app.route("/")
def index():
    return render_template("index.html")  # The upload form page


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        print("No file part in request.")
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "":
        print("No selected file.")
        return redirect(request.url)

    # Save the uploaded image to a directory
    os.makedirs("uploads", exist_ok=True)
    image_path = os.path.join("uploads", file.filename)
    file.save(image_path)

    print(f"Image saved at: {image_path}")

    # Load the image and process it using OpenCV
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Convert processed image to PIL format for pytesseract
    pil_image = Image.fromarray(thresh)

    # Extract text from the processed image
    extracted_text = pytesseract.image_to_string(pil_image)
    print(f"Extracted text: {extracted_text}")  # Print extracted text for debugging

    # Summarize the extracted text
    extracted_text = extracted_text.strip()
    if extracted_text:
        summary = summarizer(
            extracted_text, max_length=130, min_length=30, do_sample=False
        )[0]["summary_text"]
        print(f"Extracted summary: {summary}")  # Print extracted summary for debugging
    else:
        summary = "No text found in the image."

    # Pass the extracted text and summary to the result.html template
    return render_template(
        "result.html", text_in_image=extracted_text, text_summary=summary
    )


if __name__ == "__main__":
    app.run(debug=True)

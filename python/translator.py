# import os

# import cv2
# import numpy as np
# import pytesseract
# from PIL import Image
# from transformers import pipeline

# # Specify the Tesseract executable path
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# )

# # Load the image using OpenCV
# image_path = r"C:\Users\admin\OneDrive\Desktop\c#\project ad\462544078_465621719850924_6228206271450289718_n.png"


# # Check if the file exists
# if not os.path.isfile(image_path):
#     print(f"File not found: {image_path}")
# else:
#     # Read the image
#     image = cv2.imread(image_path)

#     # Check if the image was loaded correctly
#     if image is None:
#         print("Error loading image.")
#     else:
#         # Convert the image to grayscale
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#         # Apply Gaussian blur to reduce noise and improve OCR accuracy
#         blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#         # Use thresholding to get a binary image
#         _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#         # Save the processed image (optional, for debugging)
#         cv2.imwrite("processed_image.png", thresh)

#         # Convert the processed image back to PIL format for pytesseract
#         pil_image = Image.fromarray(thresh)

#         # Extract text from the processed image
#         extracted_text = pytesseract.image_to_string(pil_image)

#         # Initialize the summarizer
#         summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#         # Get the summary
#         if extracted_text.strip():  # Check if any text was extracted
#             summary = summarizer(
#                 extracted_text, max_length=130, min_length=30, do_sample=False
#             )
#             # Print the summary
#             print(summary[0]["summary_text"])
#         else:
#             print("No text found in the image.")

import os


# validate file from http request
def validate_file_from_request(request):
    if "file" not in request.files:
        print("No file part in request.")
        return None

    file = request.files["file"]

    if file.filename == "":
        print("No selected file.")
        return None

    return file


# Save the uploaded image to a directory
def save_file_to_upload(file):
    # creates a new directory called uploads if it doesnot exist
    os.makedirs("uploads", exist_ok=True)

    # generates a location to save image inside the "uploads" directory
    # e.g. if filename is "test_picture.png" then image_path will be "uploads\test_picture.png" in windows os
    image_path = os.path.join("uploads", file.filename)

    print("Image path: " + image_path)
    # saves the file in the image_path location
    file.save(image_path)
    return image_path

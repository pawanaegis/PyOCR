import os
import requests
from PIL import Image
import pytesseract
from AADHAAR_EXTRACTOR.Extractor import AadhaarExtractor


# Function to download an image from a URL and save it in the temp folder
def download_image(url, temp_folder):
    response = requests.get(url)
    if response.status_code == 200:
        image_path = os.path.join(temp_folder, 'downloaded_image.png')
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
    else:
        print(f"Failed to download image from URL: {url}")
        return None

# Function to perform OCR on an image and return extracted text
def ocr_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error during OCR: {str(e)}")
        return None

# Main function
def main():
    url = "https://i.ibb.co/w4MDvx1/1000093681-UNITED-AADHAAR.jpg"  # Replace with your image URL
    temp_folder = "tmp"  # Temporary folder to store the downloaded image

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    image_path = download_image(url, temp_folder)
    if image_path:
        obj = AadhaarExtractor(image_path)
        extracted_text = obj.extract()
        if extracted_text:
            print("Extracted Text:")
            print(extracted_text)
        else:
            print("OCR failed to extract text from the image.")

if __name__ == "__main__":
    main()

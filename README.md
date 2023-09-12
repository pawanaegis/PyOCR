# PyOCR

sudo ./aws/install
sudo ./aws/sam-installation/install
sudo apt install libgl1-mesa-glx
sudo apt install tesseract-ocr
source .venv/bin/activate
python -m ensurepip --default-pip

https://i.ibb.co/w4MDvx1/1000093681-UNITED-AADHAAR.jpg

# Function to download an image from a URL and save it in the temp folder

# def lambda_handler(event, context):

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
url = "https://i.ibb.co/w4MDvx1/1000093681-UNITED-AADHAAR.jpg" # Replace with your image URL
temp_folder = "tmp" # Temporary folder to store the downloaded image

        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        image_path = download_image(url, temp_folder)
        if image_path:
            print(image_path)
            obj = AadhaarExtractor(image_path)
            extracted_text = obj.extract()
            if extracted_text:
                print("Extracted Text:")
                print(extracted_text)
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "message": "hello world",
                        # "location": ip.text.replace("\n", "")
                    }),
                        }
            else:
                print("OCR failed to extract text from the image.")

print('hello pawan')

python -c 'import app; app.lambda_handler({
"path": "/",
"httpMethod": "GET",
"queryStringParameters": {
"url": "https://i.ibb.co/w4MDvx1/1000093681-UNITED-AADHAAR.jpg"
}
},"context")'

import os
import tempfile
import urllib.request
import pytesseract
from PIL import Image
import json
from AADHAAR_EXTRACTOR.Extractor import AadhaarExtractor

def lambda_handler(event, context):
try: # Check if the event contains a URL parameter
if 'url' not in event['queryStringParameters']:
return {
'statusCode': 400,
'body': 'Missing URL parameter'
}

        # Get the URL parameter
        url = event['queryStringParameters']['url']

        # Create a temporary directory to store the downloaded image
        temp_dir = tempfile.mkdtemp()

        # Download the image from the URL
        image_path = os.path.join(temp_dir, 'image.png')
        urllib.request.urlretrieve(url, image_path)

        # Perform OCR on the downloaded image
        image = Image.open(image_path)
        # ocr_text = pytesseract.image_to_string(image)
        obj = AadhaarExtractor(image)
        extractedData = obj.extract()
        aadhaar_numbers = []
        for data in extractedData:
            if data[1] == 'aadhaar_no' and data[3] is not None:
                aadhaar_numbers.append(data[3])

        ocr_text = list(set(aadhaar_numbers))
        aadhaar_no = ', '.join(ocr_text)

        # Clean up the temporary directory
        os.remove(image_path)
        os.rmdir(temp_dir)

        return {
            'statusCode': 200,
            'body': aadhaar_no
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

import os
import tempfile
import urllib.request
import pytesseract
from PIL import Image
import json
from AADHAAR_EXTRACTOR.Extractor import AadhaarExtractor


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
    'body': ocr_text
            }
    
except Exception as e:
return {
            'statusCode': 500,
            'body': str(e)
        }
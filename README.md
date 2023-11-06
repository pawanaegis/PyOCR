# PyOCR

sudo ./aws/install
sudo ./aws/sam-installation/install
sudo apt install libgl1-mesa-glx
sudo apt install tesseract-ocr
pyenv install 3.10.12
pyenv local 3.10.12
python -m venv my_env
source my_env/bin/activate
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

########################################################################### Re-Script for adhaar

#!/usr/bin/env python

# coding: utf-8

class AadhaarExtractor: # assume inputs are file name and not cv2 images #give underscore for private member functions # and pil images
def **init**(self, data1=None): # and pil images

        def invalidate():
            if type(data1) == str:
                import re
                if re.match(r'.*\.(jpg|png|jpeg)',data1,re.M|re.I)!= None:
                    return False
                return True
          ### check if the input string seems like a image file ###


        if type(data1)!=str :
            raise ValueError("Invalid input: Give file paths only")
        elif invalidate():
            raise ValueError("Only image files possible")

        self.data1 = data1

        # FIXED: check for invalid inputs

        self.mainlist = None

        self.process()


    def load(self, data1):  # can load and jsonify be merged?
        self.data1 = data1

        self.extract_details()

    def extract(self):
        import json
        # try:
        #     f = open(jsonpath, 'r+')
        # except FileNotFoundError:  # for the first time
        #     f = open(jsonpath, 'w+')
        # try:
        #     maindict = json.load(f)
        # except ValueError:  # for the first time
        #     print("value error")
        #     maindict = {}

        # if self.maindict['aadhaar_no'] in maindict.keys():
        #     choice = input(
        #         "This aadhar number is already present in the database:\n Do you want to update the the data for this aadhaar number (y\n)?")
        #     if choice.lower() == 'n':
        #         f.close()
        #         return self.maindict

        # maindict[self.maindict['aadhaar_no']] = self.maindict
        # f.seek(0)
        # json.dump(maindict, f, indent=2)
        # f.close()
        return self.mainlist

    def file_type(self, file):
        # import re
        # if re.match(".*\.pdf$", filePath, re.M | re.I):
        if file.content_type == r'application/pdf':
            return 'pdf'
        # if re.match(".*\.(png|jpg|jpeg|bmp|svg)$", filePath, re.M | re.I):  # changed and made more flexible
        if file.content_type == r'image/jpeg':
            return 'img'
        return 0

    def process(self):

        # if self.file_type(data) == 'pdf':
        #     dict = self.extract_from_pdf(data)
        # elif self.file_type(data) == 'img':
        self.mainlist = self.extract_from_images()
        # else:
        #     pass


    # def extract_details(self):
    #     if self.data1 != None:
    #         mainlist = self.give_details_back()

    def extract_from_images(self):
        import numpy as np
        from ultralytics import YOLO
        import cv2
        import pytesseract
        ###  specify that pytesseract needs to be explicitly installed  ###
        import random
        import logging
        import os

        logging.basicConfig(level=logging.NOTSET)

        # Get the absolute path of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the resource file
        MODEL_PATH = os.path.join(current_dir, 'best.pt')

        # MODEL_PATH = r"best.pt"

        def filter_tuples(lst):
        ##### filters the list so that only one instance of each class is present  ########

            d = {}
            for tup in lst:
                key = tup[1]
                value = tup[2]
                if key not in d:
                    d[key] = (tup, value)
                else:
                    if value > d[key][1]:
                        d[key] = (tup, value)
            return [tup for key, (tup, value) in d.items()]

        def clean_words(name):
            name = name.replace("8", "B")
            name = name.replace("0", "D")
            name = name.replace("6", "G")
            name = name.replace("1", "I")
            name = name.replace('5', 'S')

            return name

        def clean_dob(dob):
            dob = dob.strip()
            dob = dob.replace('l', '/')
            dob = dob.replace('L', '/')
            dob = dob.replace('I', '/')
            dob = dob.replace('i', '/')
            dob = dob.replace('|', '/')
            dob = dob.replace('\"', '/1')
            #       dob = dob.replace(":","")
            dob = dob.replace(" ", "")
            return dob

        def validate_aadhaar_numbers(candidate):
            if candidate == None :
                return True
            candidate = candidate.replace(' ', '')
            # The multiplication table
            d = [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
                [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
                [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
                [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
                [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
                [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
                [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
                [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
                [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            ]
            # permutation table p
            p = [
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
                [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
                [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
                [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
                [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
                [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
                [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
            ]
            # inverse table inv
            inv = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]
            # print("sonddffsddsdd")
            # print(len(candidate))
            lastDigit = candidate[-1]
            c = 0
            array = [int(i) for i in candidate if i != ' ']
            array.pop()
            array.reverse()
            for i in range(len(array)):
                c = d[c][p[((i + 1) % 8)][array[i]]]  # use verheoffs algorithm to validate
            if inv[c] == int(lastDigit):
                return True
            return False

        # file.seek(0)
        # img_bytes = file.read()
        # img_array = np.frombuffer(img_bytes, dtype=np.uint8)

        img = cv2.imread(self.data1)

        og_height,og_width,_ = img.shape

        height_scaling = og_height/640
        width_scaling = og_height/640




        # TODO for all the self.data types it should support
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        img = cv2.resize(img, (640, 640))

        # cv2.imshow("sone", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        model = YOLO(MODEL_PATH)
        results = model(img)
        # rois = []
        roidata = []

        #####     this will create a  roidata which will be list of  tuples with roi image, cls and confidence #####
        for result in results:
            #     cls = result.boxes.cls
            #     boxes = result.boxes.xyxy
            boxes = result.boxes
            for box in boxes:
                #     x1,y1,x2,y2 = box
                l = box.boxes.flatten().tolist()
                roicoords = list(map(int, l[0:4]))
                # roicoords: x1,y1,x2,y2

                confidence, cls = l[4:]
                cls = int(cls)
                #        l = list(box)
                #        x1,y1,x2,y2 = list(map(int,l))
                # print(x1, x2, y1, y2)
                # img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.putText(img, str(cls), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
                # roi = img[y1:y2, x1:x2]
                #        rois.append(roi)
                templist = [roicoords, cls,confidence]
                roidata.append(templist)
        # cv2.imshow("s", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # print(roidata)
        index = {0: "aadhaar_no",
                 1: "dob",
                 2: "gender",
                 3: "name",
                 4: "address"}

        # logging.info('BEFORE FILTERING :')
        # logging.info(len(roidata))

        # TODO there is no flag to filter roidata , introduce later
        # roidata = filter_tuples(roidata)
        # maindict = {}
        # maindict['aadhaar_no'] = maindict['dob'] = maindict['gender'] = maindict['address'] = maindict['name'] = maindict['phonenumber'] = maindict['vid'] = maindict['enrollment_number'] = None
        # logging.info('AFTER FILTERING :')
        # logging.info(len(roidata))

        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        for data in roidata:
            cls = data[1]
            x1,y1,x2,y2 = data[0]
            # data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
            random_number = random.randint(0, 1000)
            output_filename = f'output_{random_number}.jpg'

            cropped = img[y1:y2, x1:x2]
            zoomed_cropped = cv2.resize(cropped, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            #cv2.imwrite(output_filename, zoomed_cropped)
            info = pytesseract.image_to_string(cropped).strip()
            if not info:
                for brightness_change in range(5, 51, 5):  # From 5% to 50% brightness change
                    alpha = 1 - brightness_change / 100
                    beta = 0  # No change in brightness
                    adjusted_image = cv2.convertScaleAbs(cropped, alpha=alpha, beta=beta)
                    cv2.imwrite(output_filename, adjusted_image)
                    print("brightness decreased")
                    info = pytesseract.image_to_string(adjusted_image).strip()
                    if info:
                        break

            if not info:
                for brightness_change in range(5, 51, 5):  # From 5% to 50% brightness change
                    alpha = 1 + brightness_change / 100
                    beta = 0  # No change in brightness
                    adjusted_image = cv2.convertScaleAbs(cropped, alpha=alpha, beta=beta)
                    cv2.imwrite(output_filename, adjusted_image)
                    print("brightness incresaerd")
                    info = pytesseract.image_to_string(adjusted_image).strip()
                    if info:
                        break

            if not info:
                info = "not detected"

            logging.info(str(cls)+'-'+info)

            data[0][0] = x1*width_scaling
            data[0][1] = y1*height_scaling
            data[0][2] = x2*width_scaling
            data[0][3] = y2*height_scaling
          #### the scaling is reconverted to the original size dimensions  ####


            data[1] = index[cls]
            # change from indexes to name if the class

            if info != None :
                if cls == 3:
                    info = clean_words(info)

                elif cls == 1:
                    info = clean_dob(info)

                elif cls == 0:
                    info = info.replace(' ','')
                    if len(info) == 12:
                        try:
                            if not validate_aadhaar_numbers(info):
                                info = "INVALID AADHAAR NUMBER"
                        except ValueError:
                            info = None
                    else:
                        info = None

            data.append(info)

            # extracted text cleaned up :FIXED



        # TODO extract these fields too
        # maindict['phonenumber'] = None
        # maindict['vid'] = None
        # maindict['enrollment_no'] = None

        # FIXED: the coords are for 640:640 , fix it for original coords

        return roidata

    def extract_from_pdf(self, file):
        def extract_pymupdf(file):
            # Usinf pymupdf
            import fitz  # this is pymupdf
            # extract text page by page
            with fitz.open(stream=file.stream.read(), filetype='pdf') as doc:
                pymupdf_text = ""
                if (doc.is_encrypted):
                    passw = input("Enter the password")
                    # TODO display this message where?
                    doc.authenticate(password=passw)
                for page in doc:
                    pymupdf_text += page.get_text("Text")
                return pymupdf_text

        def get_details(txt):
            import re

            pattern = re.compile(
                r'Enrolment No\.: (?P<enrolment_no>[^\n]*)\nTo\n[^\n]*\n(?P<name>[^\n]*)\n(?P<relation>[S,W,D])\/O: (?P<fathers_name>[^\n]*)\n(?P<address>.*)(?P<phonenumber>\d{10})\n(?P<aadhaar_number>^\d{4} \d{4} \d{4}\n).*(?P<vid>\d{4} \d{4} \d{4} \d{4})\n.*DOB: (?P<dob>[^\n]*)\n.*(?P<gender>MALE|FEMALE|Female|Male)',
                re.M | re.A | re.S)
            # gets all info in one match(enrolment to V) which can then be parsed by the groups
            return pattern.search(txt)

        def get_enrolment_no(txt):
            return get_details(txt).group('enrolment_no')

        def get_name(txt):
            return get_details(txt).group('name')

        def get_fathers_name(txt):
            matchobj = get_details(txt)
            relation = matchobj.group('fathers_name')
            if matchobj.group('relation').lower() == 'w':
                return None
            return relation

        def get_husbands_name(txt):
            matchobj = get_details(txt)
            return matchobj.group('fathers_name')

        def get_address(txt):
            return get_details(txt).group('address')

        def get_phonenumber(txt):
            return get_details(txt).group('phonenumber')

        def get_aadhaarnumber(txt):
            return get_details(txt).group('aadhaar_number').strip()

        def get_vid(txt):
            return get_details(txt).group('vid')

        def get_gender(txt):
            return get_details(txt).group('gender')

        def get_dob(txt):
            return get_details(txt).group('dob')

        def get_details_pdf(file):
            import re
            txt = extract_pymupdf(file)
            dict = {'vid': get_vid(txt),
                    'enrollment_no': get_enrolment_no(txt),  # Fathers name':get_fathers_name(txt),
                    'name': get_name(txt),  # if dict['Fathers name'] == None :
                    'address': get_address(txt),
                    'phonenumber': get_phonenumber(txt),  # dict['Husbands name']=get_husbands_name(txt)
                    'aadhaar_no': get_aadhaarnumber(txt),
                    'sex': get_gender(txt),
                    'dob': get_dob(txt)}
            #                       ,'ID Type':'Aadhaar'}
            return dict

        return get_details_pdf(file)

if **name** == '**main**':
obj = AadhaarExtractor(r"C:\Users\91886\Desktop\cardF.jpg")
print(obj.extract()) # file = open(r"C:\Users\91886\Desktop\cardF.jpg",'r') # obj.load(file) # print(obj.to_json()) #

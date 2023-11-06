import os
import tempfile
import urllib.request
import pytesseract


ocr_text = pytesseract.image_to_string('/workspace/PyOCR/OCRAdhar/output_975.jpg')

print(ocr_text,"text")
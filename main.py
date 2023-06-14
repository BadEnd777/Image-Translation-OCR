# Written by: Pongsakorn Thipayanate
import os
import json
import pytesseract
from langdetect import detect
from googletrans import Translator
from PIL import Image, ImageDraw, ImageFont

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = config['tesseract_cmd']

# Initialize Translator
translator = Translator(service_urls=config['translator_service_urls'])

# Create output folder if it doesn't exist
os.makedirs(config['output_folder'], exist_ok=True)

# Function to detect text positions in the image
def detect_text_position(image):
    image_data = pytesseract.image_to_boxes(image, lang=config['tesseract_lang'])
    lines = image_data.split('\n')
    positions = []
    for line in lines:
        if line.strip():  # Skip empty lines
            values = line.split(' ')
            if len(values) == 6:
                _, x, y, w, h, _ = values
                x, y, w, h = int(x), int(y), int(w), int(h)
                positions.append((x, y, x + w, y + h))  # Use the original coordinates
    return positions

# Process images in the input folder
image_files = [f for f in os.listdir(config['input_folder']) if f.endswith(('.jpg', '.jpeg', '.png'))]

for image_file in image_files:
    image_path = os.path.join(config['input_folder'], image_file)
    output_path = os.path.join(config['output_folder'], f"translated_{image_file}")

    try:
        # Open the image
        image = Image.open(image_path)

        # Extract text from the image
        extracted_text = pytesseract.image_to_string(image, lang=config['tesseract_lang'])
        print("Extracted text:", extracted_text)

        # Detect the language of the extracted text
        detected_language = detect(extracted_text) if len(extracted_text) >= 5 else None

        # Translate the text if language detection was successful
        if detected_language:
            translated_text = translator.translate(extracted_text, dest=config['translation_dest']).text
        else:
            translated_text = "Language detection failed"

        print("Translated text:", translated_text)

        # Detect text positions in the image
        text_positions = detect_text_position(image)

        # Annotate the image with translated text
        draw = ImageDraw.Draw(image)
        if text_positions:
            font = ImageFont.truetype(config['font_path'], config['font_size'])
            for bbox in text_positions:
                draw.rectangle(bbox, fill='white')
                draw.text((bbox[0], bbox[1]), translated_text, fill='black', font=font)

        # Save the annotated image
        image.save(output_path)
        print("Processed image:", image_file)

    except Exception as e:
        print("Error processing image:", image_file)
        print("Error details:", str(e))

print("Image processing completed.")

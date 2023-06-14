## Image Translation OCR

This project aims to perform optical character recognition (OCR) on images and translate the extracted text into another language. The project utilizes Tesseract OCR, language detection, and Google Translate API for text translation. It supports multiple image formats (JPEG, PNG) and can process multiple images in a batch.

### Prerequisites

- [Python 3.11](https://www.python.org/downloads/) or later
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki)

### Installing

1. Clone this repository

```bash
git clone https://github.com/BadEnd777/image-translation-ocr.git
```

2. Navigate to the project directory

```bash
cd image-translation-ocr
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

### Configuration

The configuration file is located at `config.json`. The following parameters can be configured:

| Parameter                 | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `input_folder`            | The folder containing the input images.        |
| `output_folder`           | The folder to store the output images.         |
| `font_path`               | The path to the font file.                     |
| `font_size`               | The font size.                                 |
| `tesseract_cmd`           | The path to the Tesseract executable.          |
| `tesseract_lang`          | The language code for Tesseract.               |
| `translator_service_urls` | The list of URLs for the translation service.  |
| `translation_dest`        | The destination language code for translation. |

### Usage

1. Place the input images in the `input` folder.
2. Run the script

```bash
python main.py # or python3 main.py
```

3. The script will process the images one by one, extract the text, detect the language, translate the text, annotate the images with translated text, and save the processed images in the `output` folder.
4. The console will display the extracted and translated text for each image as well as any errors encountered during the process.

### Customization

- You can customize the OCR and translation settings in the config.json file to achieve better results for different languages and image types. Experiment with different Tesseract OCR configurations and translation options.
- Feel free to modify the code to add additional features, such as image preprocessing, parallel processing, or user prompts for input folder paths.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
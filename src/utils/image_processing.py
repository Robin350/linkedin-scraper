import pytesseract
import requests
import logging
import io
import re

from PIL import Image

logger = logging.getLogger(__name__)


def get_image_text(image_url):
    text = ""

    try:
        response = requests.get(image_url, stream=True)
    except Exception as e:
        logger.error(f"Unexpected error downloading image '{image_url}': {e}")
        return text

    try:
        image = Image.open(io.BytesIO(response.content))
    except Exception as e:
        logger.error(f"Unexpected error converting response from '{image_url}' to image: {e}")
        return text

    try:
        text = pytesseract.image_to_string(image)
    except Exception as e:
        logger.error(f"Unexpected error extracting text from image '{image_url}': {e}")
        return text

    text.replace("\n", " ").lower()
    text = re.sub(' +', ' ', text).strip()

    return text




import re
import requests

def is_image_url(url: str) -> bool:
    """
    Returns True if the URL is likely pointing to an image, based on:
    1. The URL ending with a common image extension (jpg, jpeg, png, gif, bmp, webp).
    2. The URL's HTTP HEAD response indicating a Content-Type starting with 'image/'.
    
    If either check passes, the function returns True.
    """
    # Check for a common image file extension
    pattern = re.compile(r'\.(jpg|jpeg|png|gif|bmp|webp)(\?.*)?$', re.IGNORECASE)
    extension_check = bool(pattern.search(url))
    
    # Check if the content type of the URL is an image using a HEAD request
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('Content-Type', '')
        content_check = content_type.startswith('image/')
    except requests.RequestException:
        content_check = False
    
    return extension_check or content_check
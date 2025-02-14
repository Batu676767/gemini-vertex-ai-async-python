import requests
import base64

def image_url_to_base64(url: str) -> str:
    """
    Fetches the image from the given URL and returns its base64 encoded string.

    Args:
        url (str): The URL of the image.

    Returns:
        str: Base64 encoded string of the image, or None if the image couldn't be fetched.
    """
    try:
        # Send a GET request to fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an exception for HTTP errors
        
        # Get the image data in binary form
        image_data = response.content
        
        # Encode the image data in base64 and decode to a UTF-8 string
        base64_str = base64.b64encode(image_data).decode('utf-8')
        return base64_str
    except requests.RequestException as e:
        print(f"Error fetching the image: {e}")
        return None
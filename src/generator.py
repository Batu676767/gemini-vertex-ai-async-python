import asyncio
import vertexai
from vertexai.generative_models import GenerativeModel

from config import GENERATION_CONFIG, SAFETY_SETTINGS, MODEL_NAME, PROJECT_ID, LOCATION
from utils.is_image_url import is_image_url
from utils.image_url_base64 import image_url_to_base64

# Initialize Vertex AI if configuration is available
if PROJECT_ID and LOCATION:
    vertexai.init(project=PROJECT_ID, location=LOCATION)
else:
    print("Warning: Missing configuration for VERTEX_AI_PROJECT or VERTEX_AI_LOCATION. Vertex AI initialization skipped.")


async def async_generate(prompt: str = "", base64_string: str = None) -> str:
    """
    Generate content using the Gemini model asynchronously.

    :param prompt: Text prompt for generation.
    :param base64_string: Base64 encoded image string, if any.
    :return: Generated text or an error message.
    """
    # Check if necessary environment configuration is available
    if not all([MODEL_NAME, PROJECT_ID, LOCATION]):
        return "Error: Missing configuration for MODEL_NAME, PROJECT_ID, or LOCATION."

    model = GenerativeModel(MODEL_NAME)
    message_content = []

    if prompt:
        message_content.append(prompt)
    if base64_string:
        message_content.append(base64_string)

    # Join the messages into a single string
    combined_message = " ".join(message_content)

    try:
        response = await model.generate_content_async(
            combined_message,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS,
            stream=False,
        )
        return response.text
    except Exception as e:
        return f"Error during content generation: {e}"


async def generate_from_input(prompt: str = "", base64_string: str = None, image_url: str = None) -> str:
    """
    Process a base64 encoded image string or image URL and generate content.

    :param prompt: Text prompt for generation.
    :param base64_string: Base64 encoded image string.
    :param image_url: URL of an image to be converted to base64.
    :return: Generated content text.
    """
    try:
        if image_url:
            if is_image_url(image_url):
                base64_string = image_url_to_base64(image_url)
                # Added check for None base64 string
                if base64_string is None:
                    return "Error: Failed to retrieve image data from the provided URL."
                image_data = f"data:image/jpeg;base64,{base64_string}"
                return await async_generate(prompt or "Describe this image", base64_string=image_data)
            else:
                return "Error: Provided image_url is not valid."

        if base64_string:
            if not base64_string.startswith("data:image/"):
                base64_string = f"data:image/jpeg;base64,{base64_string}"
            return await async_generate(prompt or "Describe this image", base64_string=base64_string)

        if prompt:
            return await async_generate(prompt)

        return "Error: Either a prompt or a base64 encoded image string must be provided."
    except Exception as e:
        return f"Error processing input: {e}"

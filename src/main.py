import asyncio
import logging
from generator import generate_from_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """
    Main function for testing the Gemini model generation.
    """
    # Load base64 string from data file
    image_url_with_file_ending = "https://techtutorialsx.com/wp-content/uploads/2019/01/esp32-arduino-core-base64-encode-string.png"
    image_url_without_fileending = (
        "https://images.asos-media.com/products/"
        "asos-design-satin-asymmetric-neck-side-bust-maxi-dress-in-burgundy/"
        "208085726-2?$n_640w$&wid=634&fit=constrain"
    )
    base64_string = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="

    tasks = [
        generate_from_input("Analyze this image and describe what you see.", base64_string=base64_string),
        generate_from_input("Analyze this image and describe what you see.", image_url=image_url_with_file_ending),
        generate_from_input("Analyze this image and describe what you see.", image_url=image_url_without_fileending)
    ]

    results = await asyncio.gather(*tasks)

    for idx, result in enumerate(results, 1):
        logger.info("Result %d: %s", idx, result)


if __name__ == "__main__":
    asyncio.run(main())

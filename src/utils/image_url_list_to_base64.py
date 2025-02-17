import asyncio
import aiohttp
from PIL import Image
import io
import math
import base64

async def fetch_image(session: aiohttp.ClientSession, url: str) -> Image.Image:
    async with session.get(url) as response:
        response.raise_for_status()
        data = await response.read()
        # Open the image and ensure it's in RGB mode
        return Image.open(io.BytesIO(data)).convert("RGB")

async def create_collage_from_urls(image_urls: list[str]) -> str:
    # Asynchronously fetch all images concurrently.
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_image(session, url) for url in image_urls]
        images = await asyncio.gather(*tasks)
    
    # Define the thumbnail size for each image
    thumb_width, thumb_height = 128, 128
    thumbnails = [img.resize((thumb_width, thumb_height)) for img in images]
    
    num_images = len(thumbnails)
    # Determine grid size (close to a square)
    grid_cols = math.ceil(math.sqrt(num_images))
    grid_rows = math.ceil(num_images / grid_cols)
    
    # Create a blank collage canvas
    collage_width = grid_cols * thumb_width
    collage_height = grid_rows * thumb_height
    collage = Image.new('RGB', (collage_width, collage_height), color=(255, 255, 255))
    
    # Paste each thumbnail into the collage grid
    for index, thumb in enumerate(thumbnails):
        row = index // grid_cols
        col = index % grid_cols
        collage.paste(thumb, (col * thumb_width, row * thumb_height))
    
    # Convert the collage image to a base64-encoded PNG string.
    buffered = io.BytesIO()
    collage.save(buffered, format="PNG")
    base64_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return base64_str


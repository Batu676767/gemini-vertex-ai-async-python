import os
from dotenv import load_dotenv

load_dotenv()

# Vertex AI configuration
PROJECT_ID = os.getenv("VERTEX_AI_PROJECT")
LOCATION = os.getenv("VERTEX_AI_LOCATION")
MODEL_NAME = os.getenv("VERTEX_AI_MODEL")

# Generation settings
GENERATION_CONFIG = {
    "max_output_tokens": 1000,
    "temperature": 1,
    "top_p": 0.95,
}

SAFETY_SETTINGS = {}

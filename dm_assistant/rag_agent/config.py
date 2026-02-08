"""
Configuration settings for the RAG Agent.

These settings are used by the various RAG tools.
Vertex AI initialization is performed here.
"""

import os
from dotenv import load_dotenv
import vertexai

# Load environment variables
load_dotenv()

# Vertex AI settings
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")

# Initialize Vertex AI
if PROJECT_ID and LOCATION:
    print(f"Initializing Vertex AI with project={PROJECT_ID}, location={LOCATION}")
    vertexai.init(project=PROJECT_ID, location=LOCATION)
else:
    raise ValueError(
        "Missing Vertex AI configuration! Please set GOOGLE_CLOUD_PROJECT and "
        "GOOGLE_CLOUD_LOCATION environment variables in your .env file.\n"
        f"Current values: PROJECT_ID={PROJECT_ID}, LOCATION={LOCATION}"
    )

# RAG settings
DEFAULT_CHUNK_SIZE = 512
DEFAULT_CHUNK_OVERLAP = 100
DEFAULT_TOP_K = 3
DEFAULT_DISTANCE_THRESHOLD = 0.5
DEFAULT_EMBEDDING_MODEL = "publishers/google/models/text-embedding-005"
DEFAULT_EMBEDDING_REQUESTS_PER_MIN = 1000
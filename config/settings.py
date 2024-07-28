import os

from dotenv import load_dotenv

load_dotenv(override=True)


GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from os import getenv
from dotenv import load_dotenv

load_dotenv()

AZURE_AI_SERVICE_ENDPOINT: str = getenv("AZURE_AI_SERVICE_ENDPOINT", "")
AZURE_AI_SERVICE_KEY: str = getenv("AZURE_AI_SERVICE_KEY", "")

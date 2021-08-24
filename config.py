import os

from dotenv import load_dotenv


load_dotenv()

CLOUDAMQP_URL = os.getenv("CLOUDAMQP_URL", default="")

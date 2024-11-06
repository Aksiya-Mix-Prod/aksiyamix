import os

from dotenv import load_dotenv

load_dotenv()

# ===================== Production/Development =====================
ENV=os.getenv("ENV")

# ===================== Dynamic Payme Payment Settings =====================
PROD_PAYME_USERNAME=os.getenv("PROD_PAYME_USERNAME")  # Get from Payme
PROD_PAYME_PASSWORD=os.getenv("PROD_PAYME_PASSWORD")  # Get from Payme
PROD_PAYME_CALLBACK_URL=os.getenv("PROD_PAYME_CALLBACK_URL") # Get from Payme

DEV_PAYME_USERNAME=os.getenv("DEV_PAYME_USERNAME") # Get from Payme
DEV_PAYME_PASSWORD=os.getenv("DEV_PAYME_PASSWORD")  # Get from Payme
DEV_PAYME_CALLBACK_URL=os.getenv("DEV_PAYME_CALLBACK_URL") # Get from Payme



PAYME_USERNAME = DEV_PAYME_USERNAME if ENV == 'development' else PROD_PAYME_USERNAME
PAYME_PASSWORD = DEV_PAYME_PASSWORD if ENV == 'development' else PROD_PAYME_PASSWORD
PAYME_CALLBACK_URL = DEV_PAYME_CALLBACK_URL if ENV == 'development' else PROD_PAYME_CALLBACK_URL
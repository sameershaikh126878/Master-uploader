import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7915889705:AAEPbxoAT65SoTwGQoEtkB1eaj4o2hBc4Uo")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "25051520"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "91c0e86e56bb2f711454d86779091033")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "5500536251").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "@DOCTOR_ASP")  # Making CREDIT an environment variable for flexibility

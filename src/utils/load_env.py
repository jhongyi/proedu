import os
from dotenv import load_dotenv

def initEnv():
    # python-dotenv
    current_path = os.path.dirname(__file__)
    dotenv_path = os.path.join(current_path, '../../config', 'django.env')
    load_dotenv(dotenv_path)
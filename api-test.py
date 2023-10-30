import os
from dotenv import load_dotenv

load_dotenv()

public_key = os.getenv('PUBLIC_KEY')
private_key = os.getenv('PRIVATE_KEY')


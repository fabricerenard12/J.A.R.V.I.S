# Test request using the RequestHandler Class
# Author: Richard Jr. Brignolle, Fabrice Renard
# Date: 15/05/2023

import dotenv
import os
from RequestHandler import RequestHandler

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
QUESTION = 'Say this is a test'

requestHandler = RequestHandler(OPENAI_API_KEY)
requestResponse = requestHandler.ask_gpt(QUESTION)

print(requestResponse)

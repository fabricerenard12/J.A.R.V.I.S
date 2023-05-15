# Request handler to handle requests to the OpenAI API
# Author: Richard Jr. Brignolle, Fabrice Renard
# Date: 15/05/2023

import requests
from requests.exceptions import HTTPError

SUCCESS_STATUS_CODE = 200
ENDPOINT_URL = 'https://api.openai.com/v1/chat/completions'

class RequestHandler:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = ENDPOINT_URL 
    
    def ask_gpt(self, prompt: str, model: str = 'gpt-3.5-turbo', temp: float = 1.0):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temp
        }
        response = requests.post(self.endpoint, headers=headers, json=data)

        if response.status_code == SUCCESS_STATUS_CODE:
            return response.json()['choices'][0]['message']['content']
        else:
            raise HTTPError(f'Error {response.status_code} : {response.text}')

import os
import requests

from flask import (
    url_for, json,
)

from app.api_secret import (
    ID, API_KEY
)

def get_api_data(word_id):
    
    # choose language
    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    response = requests.get(url, headers = {'app_id':ID, 'app_key': API_KEY})
    r_status = response.status_code

    if r_status == 200:
        data = response.json()

        word = data['results'][0]['word']
        results = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']

        return [word, results]

    else:
        return None
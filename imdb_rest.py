import json, requests

BASE_URL = "http://www.imdb.com/xml/find?json=1&nr=1&q=" #only submitting the title parameter

def lookup(name):
    print('Starting rest call for ' + name)
    response = requests.get(BASE_URL + name)
    if response.status_code == 200:
        parsed_json = json.loads(response.text)
        if 'title_popular' in parsed_json:
            return parsed_json['title_popular'][0]['title']
        else:
            return ''
    else:
        raise ValueError("Bad request!")
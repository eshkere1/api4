import requests
import os




def download_image(url, path, params):
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    response = requests.get(url, params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)
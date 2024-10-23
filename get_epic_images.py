import requests
from datetime import datetime
from download import download_image
import os
from dotenv import load_dotenv




def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    count = 5  
    payload = {"api_key": api_key, "count": count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for photo in response.json():
        date = photo.get("date")
        name = photo.get("image")        
        date = datetime.fromisoformat(date).strftime("%Y/%m/%d")
        params ={
            "api_key": api_key
        }
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png"
        download_image(url, f"images/{name}.png", params)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    get_epic_images(api_key)
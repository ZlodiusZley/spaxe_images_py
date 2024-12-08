import requests
import os
from urllib.parse import urlparse, unquote
from datetime import datetime
from save_tools import save_picture

def main(): 
    launch_id = "5eb87d42ffd86e000604b384"
    folder = 'images'
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"] 

    for image in images_url:
        response = requests.get(image)
        response.raise_for_status()

        file_name = image.split("/")[-1]  
        save_picture(folder, url, file_name)

if __name__ == "__main__":
    main()
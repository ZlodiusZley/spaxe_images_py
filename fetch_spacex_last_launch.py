import requests
import os
from urllib.parse import urlparse, unquote
from datetime import datetime
from save_tools import save_picture

def main(): 
    parser = argparse.ArgumentParser(description="Данный файл скачивает картинки с сервиcа APOD NASA")
    parser.add_argument('--folder', type=str, default='images', help='Введите название папки')
    parser.add_argument('--launch', type=str, default='5eb87d42ffd86e000604b384', help='Введите айди запуска')
    args = parser.parse_args()
    folder = args.folder
    launch_id = args.folder
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    images_url = response.json()["links"]["flickr"]["original"] 

    for image in images_url:
        file_name = image.split("/")[-1]  
        save_picture(folder, url, file_name)

if __name__ == "__main__":
    main()

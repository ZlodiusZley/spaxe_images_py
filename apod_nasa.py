import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
from datetime import datetime
from save_tools import save_picture, get_extension
import argparse


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser(description="Данный файл скачивает картинки с сервиcа APOD NASA")
    parser.add_argument('--count', type=int, default=30, help='Введите кол-во фотографий которые вы хотите скачать')
    parser.add_argument('--folder', type=str, default='images', help='Введите название папки')

    args = parser.parse_args()
    links_count = args.count
    folder = args.folder
    
    url = "https://api.nasa.gov/planetary/apod"
    params = {'api_key': nasa_api_key,'count': links_count}
    response = requests.get(url, params=params)
    response.raise_for_status()
 
    for index, nasa_image in enumerate(response.json(), 1):
        url_image = nasa_image['url']
        extension = get_extension(url_image)
        file_name = f"nasa_apod_{index}{extension}"
        save_picture(folder, url_image, file_name)


if __name__ == "__main__":
    main()

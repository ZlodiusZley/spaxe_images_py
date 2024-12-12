import requests
import os
from urllib.parse import urlparse, unquote
from datetime import datetime
from dotenv import load_dotenv
import argparse
from save_tools import save_picture, get_extension

def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser(description="Данный файл скачивает картинки с сервиcа APOD NASA")
    parser.add_argument('--folder', type=str, default='images', help='Введите название папки')

    args = parser.parse_args()
    folder = args.folder
    

    url = 'https://api.nasa.gov/EPIC/api/natural/images' 
  
    params = {'api_key': nasa_api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_epic_images = response.json()

    for index, nasa_epic_image in enumerate(nasa_epic_images, 1):
        name = nasa_epic_image['image']
        epic_image_date = nasa_epic_image['date']
        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        link_path = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{name}.png' 
        extension = get_extension(link_path)
        file_name = f"nasa_epic_{index}{extension}"
        save_picture(folder, link_path, file_name, params)


if __name__ == "__main__":
    main()



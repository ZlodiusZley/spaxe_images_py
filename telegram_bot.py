import telegram
import os
import random
import time

def main():
       folder = 'images'
       send_time = 4
       tg_token = os.getenv('TG_TOKEN')
       tg_chat_id = os.getenv('TG_CHAT_ID')
       
       bot = telegram.Bot(token=tg_token)
       while True:
              all_files = []
              for root, _, files in os.walk(folder):
                  all_files.extend([os.path.join(root, file) for file in files])
              if not all_files:
                     print(f'Папка {folder} не содержит файлов.')
                     break
       
              random_file = random.choice(all_files)
              with open(random_file, 'rb') as file:
                     bot.send_document(chat_id=tg_chat_id, document=file)
              time.sleep(send_time)

if __name__ == "__main__":
      main()

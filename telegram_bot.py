import telegram
import os
from dotenv import load_dotenv
import random
from time import sleep




def main():
    load_dotenv()
    tg_key = os.environ["TELEGRAM_KEY"]
    chat_id = os.environ["CHAT_ID"]
    bot = telegram.Bot(token=tg_key)
    while True:
        images = os.listdir("images")
        random.shuffle(images)
        for image in images:
            with open(f'images/{image}', 'rb') as f:
                bot.send_photo(chat_id=chat_id, photo=f)
            sleep(14400)




if __name__ == "__main__":

    main()
        
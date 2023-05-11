import requests
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+79963366269',
        'message': 'Hey, send me money.',
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every().day.at("09:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
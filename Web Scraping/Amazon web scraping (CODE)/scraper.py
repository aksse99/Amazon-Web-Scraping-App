import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.in/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ref=sr_1_6?crid=8GEWM8H2663U&keywords=bose+earbuds&qid=1579372938&sprefix=bose%2Caps%2C534&sr=8-6'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:4] + price[5:8])

    if(converted_price < 35400):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 35400):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('smartrishav1@gmail.com', 'xszajyrsbddaamec')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Bose-Noise-Cancelling-Headphones-Black/dp/B07Q9MJKBV/ref=sr_1_6?crid=8GEWM8H2663U&keywords=bose+earbuds&qid=1579372938&sprefix=bose%2Caps%2C534&sr=8-6'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'smartrishav1@gmail.com',
        'aksse99@gmail.com',

        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60)

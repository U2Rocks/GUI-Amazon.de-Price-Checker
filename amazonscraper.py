from bs4 import BeautifulSoup
import requests
import smtplib
from tkinter import *


# paste any full(https included) german/.de amazon ***ITEM PAGE*** url from the amazon.de website

# put your own user agent into this field
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


# defining main function that gets information form the Amazon link
def check_price():
    global itemTitle
    global itemPrice
    URL = urlentry.get()
    # if URL == default_entry or secondary_entry:
    #    urlentry.insert(END, "Please Paste in a URL...")
    #    return
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # finds product title/still has some whitespace that should be stripped()
    title = soup.find(id='productTitle').get_text().strip()
    try:
        price = soup.find(id='priceblock_ourprice').get_text().strip()
    except:
        price = "Item Price not Found"
    # converted_price = price[:-3]
    # fixed_price = float(converted_price.replace(',', '.'))
    itemTitle.config(text=title)
    itemPrice.config(text=price)

    # print(fixed_price)
    # if(fixed_price > 100000):
    #     send_mail()


# defining tkinter objects
root = Tk()
root.title("Amazon.de Price Finder")
canvas = Canvas(root, bg="black")
root.minsize(400, 300)
root.maxsize(400, 300)
title_card = Label(canvas, text="Amazon.de Price Finder",
                   bg="white", fg="black", padx=10, pady=10)

urlentry = Entry(canvas, bg="white", fg="black",
                 borderwidth=5, width=50)
default_entry = "Paste the Amazon Link Here"
secondary_entry = "Please Paste in a URL..."
urlentry.insert(END, default_entry)
urlButton = Button(canvas, bg="#17ae29", fg="#ffffff", padx=20,
                   pady=10, text="Click Here to Find Price!", command=check_price)

itemTitle = Label(canvas, bg="white", fg="black", padx=10, pady=10,
                  text="Your Amazon Item Name is...", font=("Arial", 12), wraplength=400)
itemPrice = Label(canvas, bg="white", fg="black", padx=10,
                  pady=10, text="Your Amazon Price is...", font=("Arial", 20))

# packing tkinter objects to screen
canvas.pack()
title_card.pack()
urlentry.pack()
urlButton.pack()
itemTitle.pack()
itemPrice.pack()


# function for sending an email if a amazon price gets low enough
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('fakesender@gmail.com', '***put app password here***')

    subject = 'Price fell down!'
    body = 'Check the amazon link! https://www.amazon.de/Sony-Vollformat-Digitalkamera-Megapixel-SEL-2870/dp/B00FWUDEEC/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1628106924&sr=8-6'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'fakesender@gmail.com',
        'fakerecipient@gmail.com',
        msg
    )
    print('Email Sent')
    server.quit()


while(True):
    root.mainloop()

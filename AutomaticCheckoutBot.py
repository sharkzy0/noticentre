import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import schedule
import time

# URL of the website to check
URL = input("Type in the URL for the desired Webiste:")

# Desired item name
ITEM_NAME =input("Type in the exact name for the desired product:")

# Email settings
EMAIL_ADDRESS =input("Where do you want recive the email from:")
EMAIL_PASSWORD = input("What is the password to your email:")
TO_EMAIL = input("Where do you want recive the email:")


def check_for_item():
    # Make a request to the website
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Search for the item name in the HTML
    if ITEM_NAME in soup.text:
        # Send an email notification
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"The item {ITEM_NAME} is now available at {datetime.now()}!"
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)
        server.quit()
        print(f"Email sent at {datetime.now()}")
    else:
        print(f"Item not found at {datetime.now()}")


# Schedule the check_for_item function to run every 24 hour# )
schedule.every(450).minutes.do(check_for_item)
while True:
    schedule.run_pending()
    time.sleep(1)
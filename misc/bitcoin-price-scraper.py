# bitcoin price scraper by kenny zhang

import requests
from bs4 import BeautifulSoup

def get_bitcoin_price():
    url = "https://www.coindesk.com/price/bitcoin/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    price_element = soup.find("span", class_="currency-pricestyles__Price-sc-1v249sx-0 jobFak")
    
    if price_element is None:
        print("Error: Could not find the price.")
    else:
        price = float(price_element.text.strip().replace(",", ""))
        print(f"${price}")

if __name__ == "__main__":
    get_bitcoin_price()

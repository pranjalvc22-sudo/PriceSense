import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # Try multiple selectors
        price = soup.find("span", {"class": "a-price-whole"})

        if price:
            return int(price.text.replace(",", ""))

        # fallback selector
        price = soup.find("span", {"id": "priceblock_ourprice"})
        if price:
            return int(price.text.replace("₹", "").replace(",", ""))

        return None

    except:
        return None
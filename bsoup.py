import bs4
import requests

# res = requests.get("https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/")
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, "html.parser")
# soup.select('')
# print(soup)

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right')
    return elems[0].text.strip()

price = getAmazonPrice('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print(f"The price is {price}")

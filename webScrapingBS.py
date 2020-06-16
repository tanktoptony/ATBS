import bs4, requests

def getNordstromPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body div#root div.navigation-mouse.browser-firefox.browser-firefox-77.os-unknown main#layer-0.jbP5M div.ZUQSI._2CAJk div._1JtW7._2VF_A._2wqvV div._1LLlW._20Uii div._24Msd._3S05U._21MUS div#selling-essentials._3XEVq._3-30B div div._1vV3F section#product-page-price-lockup span span#current-price-string._1ds4c')
    return elems[0].text.strip()

price = getNordstromPrice('https://shop.nordstrom.com/s/nordstrom-mens-shop-3-pack-classic-fit-boxers/3341452?origin=category-personalizedsort&breadcrumb=Home%2FSale%2FMen&color=blue%20dazzle%20solid-%20plaid%20pack')

print('The price is ' + price)

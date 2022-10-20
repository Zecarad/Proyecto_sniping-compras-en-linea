from time import sleep

from requests_html import HTMLSession

url = "https://extremetechcr.com/tienda/componentes/8036-msi-optix-ag321cqr-32-rgb-2k-165hz-freesync.html"

session = HTMLSession()

while True:
    r: session.get(url)
    buy_zone = r.html.find("#btnWishAddBuy")
    if len(buy_zone) > 0:
        print("Stock disponible")
    else:
        print("No hay stock")

    sleep(30)
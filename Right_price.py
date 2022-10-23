import random

from Price_camparation import speak, listen
from requests_html import HTMLSession

def hear_and_listen():
    while True:
        try:
            price = listen()
            price = price.replace("€", "").replace(",",".").replace("con",".")
            final_price = float (price)
            return  final_price
        except ValueError:
            print("Precio no aceptado")


def get_random_attribute():
    session = HTMLSession()
    web_site = session.get("https://www.coolmod.com/")
    categories = web_site.html.find(".subfamilyheadertittle")
    category = random.choice(categories)

    while category.text == "Configura tu PC a Medida":
        category = random.choice(categories)

    product_page = session.get(category.attrs["href"])
    products = product_page.html.find(".c-data-product-list")

    product = random.choise(products)
    img_src = product.find("sc-cTkxnA imhGni sc-hScDBe fOBkwd", first=True).attrs["src"]
    product_name = product.find("data-product-name", first=True).text
    product_price = product.find("data-product-price", first=True).text

    final_price = float(product_price.replace("€", "").replace(",","."))

    return img_src, product_name, final_price



def main():
    speak("Bienvenido al programa, vamos a verificar precios")
    img_src, product_name, final_price = get_random_attribute()
    speak("El nombre del producto es {}, cuanto crees que vale?".format(product_name))
    print(product_name)
    user_guess = hear_and_listen()
    speak("El precio era {}".format(final_price))




if __name__ =="__main__":
    main()
from time import sleep
from selenium import webdriver
from requests_html import HTMLSession
from webdriver_manager.firefox import GeckoDriverManager

##url = "https://extremetechcr.com/tienda/componentes/8036-msi-optix-ag321cqr-32-rgb-2k-165hz-freesync.html"
url = "https://www.coolmod.com/vga-msi-rtx-3070-suprim-x-8g-lhr-nv-rtx3070-gddr6-8gb-256bit-3dp-1hdmi-torx-fan-3-0-3-ventiladores/"


session = HTMLSession()

while True:
    r = session.get(url)
    buy_zone = r.html.find("#productBuyButtons")




    #sleep(30)
    if len(buy_zone) > 0:
        print("Stock disponible")
        river = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        river.get(url)

        sleep(5)
        river.find_element_by_class_name("button coolprimarybutton px-3 py-1 mt-1").click()
        river.find_element_by_class_name("fas fa-cart-arrow-down").click()
        river.find_element_by_class_name("button-buy").click()
        sleep(1)
        river.find_element_by_class_name("confirm").click()
        river.find_element_by_class_name("button-buy").click()
    else:
        print("No hay stock")
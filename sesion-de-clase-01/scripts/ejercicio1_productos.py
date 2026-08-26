from tienda_scraper.scraper import obtener_soup
from tienda_scraper.parser import parse_productos
from tienda_scraper.writer import write_to_csv
from tienda_scraper.config import URL_PRODUCTOS, OUTPUT_PRODUCTOS, OUTPUT_PRODUCTOS_STOCK

if __name__ == "__main__":
    soup = obtener_soup(URL_PRODUCTOS)

    if soup:
        productos = parse_productos(soup)

        for producto in productos:
            print(producto["codigo"], producto["nombre"], producto["precio"], producto["stock"], producto["calificacion"])

        write_to_csv(productos, OUTPUT_PRODUCTOS)

        productos_stock = [prod for prod in productos if prod["stock"] < 20]
        write_to_csv(productos_stock, OUTPUT_PRODUCTOS_STOCK)


    print("El scraping de productos ha finalizado.")

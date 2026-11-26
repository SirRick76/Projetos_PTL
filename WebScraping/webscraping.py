import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Definir o endereço do site
url="https://books.toscrape.com/"

while url:
    #Fazer o pedido ao site
    resposta= requests.get(url)
    resposta.encoding = "utf-8"
    print(type(resposta))
    print("codigo", resposta.status_code)
    print(resposta.url)
    print(resposta.headers)

    #Analisar o HTML
    soup = BeautifulSoup(resposta.text, "html.parser")

    #Encontrar todos os livros
    livros=soup.find_all("article", class_="product_pod")
    print(type(livros))

    classificacoes={
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    #Extrair e apresentar os nomes
    for livro in livros:
        nome=livro.find("h3").find("a")["title"]
        #Extrair o preco
        preco=livro.find("p", class_="price_color").text
        #Extrair a disponibilidade em stock
        stock=livro.find("p", class_="instock availability").text.strip()
        #Extrair o rating
        rating=livro.find("p",class_="star-rating")["class"]
        rating = rating[1] # o texto do numero
        rating= classificacoes[rating]
        print("Livro:", nome)
        print("Preco:", preco)
        print("Disponibilidade:", stock)
        print("Rating:", rating)
        print("---------------------------------")
    pagina_seguinte=soup.find("li",class_="next")
    if pagina_seguinte:
        link=pagina_seguinte.find("a")["href"]
        #construir o endereço
        url=urljoin(resposta.url,link)
    else:
        #nao existe mais paginas
        url=None



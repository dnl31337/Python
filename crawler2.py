from bs4 import BeautifulSoup, Comment
import requests
import sys

# Funcao para o crawler
def crawl(url):

    lista_urls = []
    visitadas = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    # links na pagina inicial
    for link in soup.find_all('a',href=True):
        if str(url) in link.get('href'):
	    x = link.get('href').encode('utf-8')
	    lista_urls.append(x)

    with open('aker.com.br-links.txt','a') as f:
        for link in lista_urls:
            f.write(link)
            f.write('\n')


    # comentarios da pagina inicial
    comentarios = soup.findAll(text=lambda text:isinstance(text, Comment))
    with open ('aker.com.br-comentarios.txt','a') as w:
        for com in comentarios:
            w.write(com)
            w.write('\n')


    # palavras da pagina inicial
    palavras = soup.findAll(text=True)
    palavras = list(set(palavras))
    with open ('aker.com.br-palavras.txt','a') as w:
        for p in palavras:
            x = p.encode('utf-8')
            w.write(x)
            w.write('\n')

    lista_urls = list(set(lista_urls))

    # parseando recursivamente
    while len(lista_urls) > 0:
        for pagina in lista_urls:
            try:
                r = requests.get(pagina)
                lista_urls.remove(pagina)
                visitadas.append(pagina)
                soup2 = BeautifulSoup(r.content)

                # pegando os links
                for link in soup2.find_all('a',href=True):
                    if str(url) in link.get('href'):
                        x = link.get('href').encode('utf-8')
                        if x not in lista_urls and x not in visitadas:
                            lista_urls.append(x)

                # pegando os comentarios
                comentarios2 = soup2.findAll(text=lambda text:isinstance(text, Comment))
                with open ('aker.com.br-comentarios.txt','a') as w:
                    for com in comentarios2:
                        w.write(com)
                        w.write('\n')

                # pegando as palavras
                palavras2 = soup2.findAll(text=True)
                palavras2 = list(set(palavras))
                with open('aker.com.br-palavras.txt','a') as w:
                    w.write(p)
                    w.write('\n')

            except:
                pass

    # salvando paginas crawleadas
    with open('aker.com.br-links.txt','a') as f:
        for url in visitadas:
            f.write(url)
            f.write('\n')


    # retirando links repetidos do arquivo
    uniqlines = set(open('aker.com.br-links.txt').readlines())
    bar = open('aker.com.br-links.txt', 'w').writelines(set(uniqlines))

    uniqlines = set(open('aker.com.br-palavras.txt').readlines())
    bar = open('aker.com.br-palavras.txt', 'w').writelines(set(uniqlines))


def main():

    if len(sys.argv) != 2:
        print '..m.Eu...cR4W.l.e.R.....01'
        print 'python meu_crawler.py http://www.teste.com.br'
        sys.exit(-1)
    url = sys.argv[1]
    crawl(url)

if __name__ == "__main__":
    main()

'''


# comentarios da pagina inicial
comentarios = soup.findAll(text=lambda text:isinstance(text, Comment))
with open ('aker.com.br-comentarios.txt','wb') as w:
	for com in comentarios:
		#print com.extract()
		w.write(com)
		w.write('\n')


# escrevendo arquivo com o link
with open ('aker.com.br-links.txt','wb') as f:
	for link in urls:
		f.write(link)
		f.write('\n')
'''










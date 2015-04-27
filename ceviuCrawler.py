 # -*- coding: utf-8 -*-
'''
C3V1U CR4WL3R 1.0
Visa buscar as vagas de TI do ultimo mês em Brasília-DF, no site de empregos CEVIU.
Ordena das vagas mais atuais até as vagas mais antigas do mês.
Autor: dani3l alm3ida
dnl31337@gmail.com
'''
import requests
from bs4 import BeautifulSoup

# Credenciais de acesso
payload = {
        'perfil':'',
        'action':'doLogin',
        'login':'seu@login.com',
        'senha':'suaSenha'
        }

# Proxy para testar as requisicoes
proxies = {
        "http":"http://127.0.0.1:8008",
        "https":"http://127.0.0.1:8008"
        }

with requests.Session() as req:
    
    # Primeira requisicao pra pegar o cookie da sessao
    req.get('http://www.ceviu.com.br')

    # Login
    req.post('http://www.ceviu.com.br:80/login/',data=payload)

    # Requisicoes para filtrar para Brasilia, listar o ultimo mes, e ordernar por dada.    
    req.get('http://www.ceviu.com.br/buscar/empregos?level=0&facetEstado%5B%5D=DF&labelEstado=Estado%2FRegi%E3o&termoFiltraEstadoRegiaoMacro=DF&q=&termoFiltraEstado=DF&itensPagina=20&i=true?termoData=&termoPesquisa=&itensPagina=20&ini=0&ordenar=&level=2')
    req.get('http://www.ceviu.com.br/buscar/empregos?level=2&empresaId=&labelTipoVaga=&realTipoVaga=&labelData=&qtDias=&labelCidade=&labelCargos=&labelMacroNivel=&labelDeficiencia=&realDeficiencia=&labelSalario=&faixaSal=&termoPesquisa=&ordenar=data+desc&itensPagina=20&ini=0&pages=0')
    payload = {
            'url':'http://www.ceviu.com.br/buscar/empregos?level=2&empresaId=&labelTipoVaga=&realTipoVaga=&labelData=&qtDias=&labelCidade=&labelCargos=&labelMacroNivel=&labelDeficiencia=&realDeficiencia=&labelSalario=&faixaSal=&termoPesquisa=&ordenar=data+desc&itensPagina=20&ini=0&pages=0?termoData=&termoPesquisa=&itensPagina=20&ini=0&ordenar=data desc&level=2'
            }
    req.post('http://www.ceviu.com.br/buscar/facets',data=payload)
    html = req.get('http://www.ceviu.com.br:80/buscar/empregos?level=0&empresaId=&labelTipoVaga=&realTipoVaga=&labelData=Data&qtDias=30&labelMacroNivel=&labelDeficiencia=&realDeficiencia=&faixaSal=&termoData=%DAltimo+m%EAs&termoPesquisa=&ordenar=data+desc&itensPagina=20&ini=0&pages=0')

    # Parseador do html
    soup = BeautifulSoup(html.content)
        
    # Extraindo total de vagas
    vagas = str(soup.find("div", {"class":"quantidade_pag"}).get_text().encode('utf-8').strip()[6:])
    vagas = int(vagas.strip('\xc2\xa0'))

    # Calculo para ver total de requisicoes
    totalreq = vagas
    while totalreq % 20 != 0:
        totalreq+=1
    totalreq = totalreq / 20

    
    print '\n0x C3V1U CR4WL3R 1.0 - vAGaS bRAsILia - uLTimO mES - dAnI3L aLM3idA\n'
    
    print 'Total de vagas: '+str(vagas)
    print 'Numero de paginas: '+str(totalreq)

    lista = []
    listadata = []
    a=0

    for link in soup.findAll('a', href=True):
        if '/buscar/vaga/' in link['href']:
            #print link['href'] + " Titulo: " + link.get_text() 
            #print(link['href'].split('-')[1])
            #print link['href'].split('-')[1]
            num = int(link['href'].split('-')[1])
            lista.append(num)           
            #print link.get_text()+'  '+link['href']
            s = "descricao"+str(lista[a])
            teste = str(soup.find("div",{"id":s}).get_text().encode('utf-8'))
            teste = teste[17:]
            #print (teste)
            data = str(soup.find("strong").get_text().encode('utf-8'))
            listadata.append(data)
            #data = data[35:45]
            print (data)
            a+=1   

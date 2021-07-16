from selenium import webdriver
import pyautogui as pg
import webbrowser as web
import time as tm
import requests
import unicodedata
from googlesearch import search



driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

while True:
    name = input('Usuario : ')
    msg = input('mensaje : ')

    input('presiona enter')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('DuUXI')


    tm.sleep(3)

    mensaje = msg.split(' ')
    pags = []

    for url in search(msg):
        pags.append(url)

    pag = requests.get(pags[0])
    pagina = pag.text

    pag1 = requests.get(pags[1])
    pagina1 = pag1.text

    pag2 = requests.get(pags[2])
    pagina2 = pag2.text

    pag3 = requests.get(pags[3])
    pagina3 = pag3.text

    pag4 = requests.get(pags[4])
    pagina4 = pag4.text



    def strip(texto):
        try:
            texto = unicode(texto, 'utf-8')
        except NameError:
            pass
        texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
        return str(texto)

    cont = 0
    for i in mensaje:
        if i in pagina:
            cont += 1
        else:
            continue

    cont1 = 0
    for i in mensaje:
        if i in pagina1:
            cont1 += 1
        else:
            continue
        
    cont2 = 0
    for i in mensaje:
        if i in pagina2:
            cont2 += 1
        else:
            continue

    cont3 = 0
    for i in mensaje:
        if i in pagina3:
            cont3 += 1
        else:
            continue

    cont4 = 0
    for i in mensaje:
        if i in pagina4:
            cont4 += 1
        else:
            continue

    porcentaje = (cont/len(mensaje))*100
    porcentaje1 = (cont1/len(mensaje))*100
    porcentaje2 = (cont2/len(mensaje))*100
    porcentaje3 = (cont3/len(mensaje))*100
    porcentaje4 = (cont4/len(mensaje))*100



    if porcentaje >= 100:
        texto = strip(msg)
        verif = "MENSAJE VERIFICADO // " + str(texto)+' '+ str(pags[0])
        pg.write(verif)
        tm.sleep(5)
        pg.press('enter')
        tm.sleep(5)
        pg.press('enter')
        exit()
    elif porcentaje1 >= 100:
        texto = strip(msg)
        verif = "MENSAJE VERIFICADO // " + str(texto) +' '+ str(pags[1])
        pg.write(verif)
        tm.sleep(5)
        pg.press('enter')
        tm.sleep(5)
        pg.press('enter')
        exit()
    elif porcentaje2 >= 100:
        texto = strip(msg)
        verif = "MENSAJE VERIFICADO // " + str(texto) +' '+ str(pags[2])
        pg.write(verif)
        tm.sleep(5)
        pg.press('enter')
        tm.sleep(5)
        pg.press('enter')
        exit()
    elif porcentaje3 >= 100:
        texto = strip(msg)
        verif = "MENSAJE VERIFICADO // " + str(texto) +' '+ str(pags[3])
        pg.write(verif)
        tm.sleep(5)
        pg.press('enter')
        tm.sleep(5)
        pg.press('enter')
        exit()
    elif porcentaje4 >= 100:
        texto = strip(msg)
        verif = "MENSAJE VERIFICADO // " + str(texto) +' '+ str(pags[4])
        pg.write(verif)
        tm.sleep(5)
        pg.press('enter')
        tm.sleep(5)
        pg.press('enter')
        exit()
    else:
        texto = strip(msg)
        noverif = "MENSAJE NO VERIFICADO // " + str(texto)
        pg.write(noverif)
        pg.press('enter')



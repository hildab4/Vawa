from selenium import webdriver
import pyautogui as pg
import webbrowser as web
import time as tm
import requests
import unicodedata
from googlesearch import search
import sys
 

print('Programa para la verificacion de mensajes para evitar difamacion de fake news')
print('1.-Mandar whatsapp')
print('2.-Mandar DM en Instagram')
print('3.-Salir del programa')
while True:
    pregunta=int(input("¿Que operacion quieres realizar?"))
    if pregunta ==1:
        import Waweb
    elif pregunta ==2:
        import Instagram
    elif pregunta ==3:
        sys.exit()
    

from selenium import webdriver
from openpyxl import Workbook
from openpyxl import load_workbook
import os
import time
import datetime

'''
Este script se conecta a la pagina web de Google Apps Store que el usuario haya seleccionado
y extrae una lista de las los datas correspondientes al nombre de usuario, comentario y 
fecha del copmentario'''

driver = webdriver.Firefox(executable_path = 'C:\\WebDrivers\\geckodriver.exe')
base_url = input("Escribir la URL de la App: ")
url = (base_url)
driver.get(url)
time.sleep(1)

lista = [ ]
#Realiza una lista de los datos extraidos de la pagina seleccionada
names = driver.find_elements_by_xpath("//span[contains(@class,'X43Kjb')]")
for name in names:
    n = name.text
    lista.append(n)
comments = driver.find_elements_by_xpath("//span[contains(@jsname,'bN97Pc')]")
for comment in comments:
    c = comment.text
    lista.append(c)

dates = driver.find_elements_by_xpath("//span[contains(@class,'p2TkOb')]")
for date in dates:
    d = date.text
    lista.append(d)

#Abre el archivo excel correspondiente a las aplicaciones extraidas
book = Workbook()
sheet = book.active

workbook_name = 'Applications.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

page.append(lista)

wb.save(filename=workbook_name)

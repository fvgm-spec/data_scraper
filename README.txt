Para ejecutar el programa que extrae las aplicaciones de AppStore Google, como primer requisito debe 
tener instalado Python 3.9 y las librerias de python selenium, openpyxl, para instalarlos en la consola de windows introducir los comandos pip install selenium y pip install openpyxl, luego de haber instalado python.

Descargar el driver para firefox del link (https://github.com/mozilla/geckodriver/releases) y guardarlo en la ruta C:/WebDrivers de su computador.

Como segundo paso comenzar a ejecutar los archivos .bat appstore.bat y extraer.bat, estos archivos ejecutaran automaticamente el proceso de llenar con los datos a los archivos excel AppStoreList.xlsx y Applications.xlsx.

Al ejecutar el bat appstore, se llenara con una listya de urls correspondientes a las aplicaciones en el appstore de google, abrir este archivo excel y aplicar la macro.xlsm para darle un formato adecuado.

Luego de ello se puede ejecutar el bat extraer.bat, en cual en la consola de windows solicita la url de la app de la cual desea extrer informacion, (las urls de las apps se encuentran en el archivo excel AppStoreList.xlsx), copiar la url deseada del archivo excel y pegarla dando solo click derecho del mouse en el espacio solicitado de la consola y presionar enter.

Automaticamente abre una ventana del navegador Firefox, desde la cual se extarera la infpormacion deseada en el archivo excel Applications.xlsx, luego de ello abrir este archivo y aplicar la macro anterior para darle formato.

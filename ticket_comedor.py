print("Arranca")
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
dni="dni"
passwd="contraseña"
driver_path='path al chrome driver' #Direccion del webdriver
options = webdriver.ChromeOptions() #Variable de las opciones del webdriver
#options.headless = True #Para que no se vea la ventana del navegador
driver = webdriver.Chrome(executable_path=driver_path,options=options) #ejecutar webdriver
print("Ejecuto el webdriver")
driver.get("https://comedores.unr.edu.ar/") #Carga la página
print("Carga la página")
driver.implicitly_wait(10) #Espera que cargue la página
dni_campo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[1]/input') #Busco el campo de dni
print("Encontre el campo del dni")
passwd_campo = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/form/div[1]/div[2]/input') #Busco el campo de la pass
print("Encontre el campo de la pass")
boton_ingresar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/form/div[2]/button') #Busco el boton de ingreso
print("Encontre el boton para ingresar")
dni_campo.send_keys(dni)
print("Escribo dni")
sleep(2)
passwd_campo.send_keys(passwd)
print("Escribo contraseña")
sleep(2)
print("Voy a apretar el boton de ingreso")
driver.execute_script("arguments[0].click();", boton_ingresar) #Apreto el boton de ingreso
sleep(10)
with open('almuerzo.png', 'wb') as file: #Creo el archivo
#Identifico el elemento
   almuerzo = driver.find_element(By.XPATH,'//*[@id="inicio"]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/img')
#Escribo el archivo con el elemento
   file.write(almuerzo.screenshot_as_png)
print("Guardo almuerzo")
boton_siguiente = driver.find_element(By.XPATH, '//*[@id="inicio"]/div[2]/div[1]/div/div[2]/div/div[2]/button[2]/i') #Identifico boton de siguiente
sleep(1)
driver.execute_script("arguments[0].click();", boton_siguiente) #Apreto el boton de ingreso
sleep(1)
with open('cena.png', 'wb') as file: #Creo el archivo
#Identifico el elemento
    cena = driver.find_element(By.XPATH,'//*[@id="inicio"]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/img')
#Escribo el archivo con el elemento
    file.write(cena.screenshot_as_png)
print("Guardo la cena")
driver.quit()  #Cierro el navegador cuando termina el for
print("Terminó")

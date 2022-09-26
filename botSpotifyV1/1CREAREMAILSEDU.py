# -*- coding: utf-8 -*-
#TESTTTTT

import random
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesCheckaccount import Acciones
from threading import Thread, Barrier
import time

hilos=1
start= time.time()


def iniciarbot(cedula,nombre,apellido1,apellido2,sexo,dia,mes,ano,telefono,usuario,email):

    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)

    acciones.primerapagina(cedula,nombre,apellido1,apellido2,sexo,dia,mes,ano,telefono,email)
    time.sleep(2)
    acciones.segundapagina(cedula)
    time.sleep(3)
    acciones.tercerapagina()
    time.sleep(3)
    acciones.cuartapagina(usuario)
    time.sleep(180)          

    db.updateOne("gmail",datos[0]["_id"],"item","OK")
    print ("CUENTA CREADA OK")
    db.cerrarConexion()
    driver.close()
    
hilos=1
db=MongoDB(hilos)
db.iniciarDB()

item=random.randint(0,9999)
datos= db.findby1("gmail","item",item)
item=datos[0]["item"]*-1
db.updateOne("gmail",datos[0]["_id"],"item",item)


datos= db.findby1("gmail","item",item)
print(datos)
diaNac=str(random.randint(1,28))
mesNac=str(random.randint(1,12))
anionaci=str(random.randint(1999,2002))

telefono=f"320{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"


for elem in datos:
    CEDULA=elem["cedula"]
    NOMBRE=elem["NOMBRE"]
    PRIMERAPELLIDO=elem["PRIMERAPELLIDO"]
    SEGUNDOAPELLIDO=elem["SEGUNDOAPELLIDO"]
    sexasp=elem["sexasp"]
    USUARIO=elem["USUARIO"]
    EMAIL=elem["EMAIL"]
    
    print(item,CEDULA,  NOMBRE, PRIMERAPELLIDO, SEGUNDOAPELLIDO, sexasp, diaNac, mesNac, anionaci,telefono,USUARIO,EMAIL)
try:    
    iniciarbot(CEDULA,  NOMBRE, PRIMERAPELLIDO, SEGUNDOAPELLIDO, sexasp, diaNac, mesNac, anionaci,telefono,USUARIO,EMAIL)
except:
    item=datos[0]["item"]*-1
    db.updateOne("gmail",datos[0]["_id"],"item",item)
    exit()




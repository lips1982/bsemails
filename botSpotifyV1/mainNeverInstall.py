# -*- coding: utf-8 -*-
import Xlib.display
from pyvirtualdisplay import Display
import pyautogui
import os
from PQTs.Paths import pathImg
import random
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesCheckaccount import Acciones

import time

def main():


    #--> Descomentar para ver en PC
    #display = Display(visible=True, size=(1200,768))

    display = Display(visible=True, size=(1900,1268), backend="xvfb", use_xauth=True)

    display.start()

    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    hilos=1
    def iniciarbot(cedula,diaExp,mesExp,anioExp,diaNac,mesNac,anionaci,NOMBRE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,sexasp,EMAIL,telefonofijo,telefonomivil):
        try:
            driver = BaseConexion().conexionChrome()
            #driver = BaseConexion().conexionChromeHeadless()

            acciones = Acciones(driver)
            print("ingresando primera pagina")
            acciones.primerapagina(cedula)
            #print("ingresando segunda pagina")
            #acciones.segundapagina()
            print("ingresando tercera pagina")
            acciones.tercerapagina(diaExp,mesExp,anioExp,diaNac,mesNac,anionaci,NOMBRE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,sexasp,EMAIL,telefonofijo,telefonomivil)
            print ("fin de paginas...")
            db.iniciarDB()
            db.updateOne("gmail",datos[0]["_id"],"item","OK")
            print ("CUENTA CREADA OK")
            db.cerrarConexion()
            driver.close()
        except Exception as e:
            db.iniciarDB()
            item=datos[0]["item"]*-1
            db.updateOne("gmail",datos[0]["_id"],"item",item)
            print(e)
            driver.close()


    hilos=1
    db=MongoDB(hilos)
    db.iniciarDB()
    listaa=[1364,1389,1894,1899,1901,1905,1907,1916,1918,1923,1926,1937,1939,1940,1945,1951,1952,1954,1966,1968,1969,1970,1973,1974,1982,1984,1991,1993,2004,2015,2024,2025,2027,2029,2031,2033,2039,2041,2042,2047,2048,2049,2050,2053,2055,2056,2062,2069,2075,2079,2083,2086,2096,2100,2106,2107,2108,2110,2111,2112,2120,2122,2124,2128,2129,2131,2141,2142,2151,2155,2157,2163,2164,2168,2169,2174,2177,2179,2180,2182,2186,2191,2205,2207,2208,2210,2214,2218,2225,2235,2237,2240,2245,2250,2252,2253,2263,2266,2275,2276,2277,2283,2284,2287,2288,2296,2299,2300,2301,2307,2308,2310,2314,2321,2323,2328,2330,2331,2335,2336,2338,2339,2342,2343,2345,2347,2350,2362,2369,2372,2373,2386,2393,2396]
    item=random.choice(listaa)
    datos= db.findby1("gmail","item",item)
    if len(datos)==0:
        print("no hay datos")
        exit()
    item=datos[0]["item"]*-1
    db.updateOne("gmail",datos[0]["_id"],"item",item)
    db.cerrarConexion()
    convocatoria= "2022-1A - 33"
    diaExp=str(random.randint(1,28))
    mesExp=str(random.randint(1,12))
    anioExp=str(random.randint(2019,2021))
    diaNac=str(random.randint(1,28))
    mesNac=str(random.randint(1,12))
    anionaci=str(random.randint(1999,2002))
    idPaissNac="170"
    idProvinciaNac="11"
    idLocalidadNac="1"
    idLocalidadCur ="1"  #CIUDAD DE RESIDENCIA
    telefonofijo=f"601{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"
    telefonomivil=f"320{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}"

    for elem in datos:
        CEDULA=elem["cedula"]
        NOMBRE=elem["NOMBRE"]
        PRIMERAPELLIDO=elem["PRIMERAPELLIDO"]
        SEGUNDOAPELLIDO=elem["SEGUNDOAPELLIDO"]
        sexasp=elem["sexasp"]
        EMAIL=elem["EMAIL"]
        
        print(CEDULA, NOMBRE, PRIMERAPELLIDO, SEGUNDOAPELLIDO, sexasp, EMAIL)

        iniciarbot(CEDULA,diaExp,mesExp,anioExp,diaNac,mesNac,anionaci,NOMBRE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,sexasp,EMAIL,telefonofijo,telefonomivil)

    display.stop()

if __name__ == '__main__':
    i=1
    while i<=3:
        try:
            main()
            time.sleep(random.randint(300,400))
            i+=1
        except Exception as e:
            print(e)






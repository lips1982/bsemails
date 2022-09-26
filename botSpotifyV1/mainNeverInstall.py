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
    listaa=[4,37,113,210,286,329,330,336,359,473,655,695,707,738,741,982,1010,1079,1235,1237,1244,1245,1247,1253,1257,1258,1259,1261,1269,1276,1285,1286,1291,1295,1297,1303,1308,1311,1316,1317,1322,1324,1326,1329,1333,1338,1339,1343,1346,1349,1354,1356,1357,1361,1364,1366,1367,1371,1381,1386,1389,1391,1399,1400,1402,1404,1411,1412,1416,1425,1428,1431,1433,1434,1437,1440,1449,1450,1451,1457,1462,1464,1465,1472,1473,1474,1480,1481,1482,1485,1487,1504,1512,1513,1514,1515,1517,1520,1523,1525,1529,1531,1533,1535,1537,1538,1542,1544,1545,1547,1552,1553,1554,1555,1556,1559,1560,1561,1562,1565,1571,1578,1579,1590,1595,1597,1599,1601,1602,1604,1609,1616,1622,1623,1628,1644,1654,1655,1657,1658,1662,1666,1667,1668,1670,1673,1679,1680,1685,1689,1691,1694,1695,1700,1710,1713,1715,1716,1717,1730,1731,1734,1738,1739,1744,1746,1754,1760,1762,1763,1765,1766,1769,1771,1776,1778,1787,1791,1793,1796,1808,1815,1816,1831,1836,1837,1842,1854,1855,1859,1863,1867,1868,1874,1877,1882,1889,1894,1896,1897]
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






# -*- coding: utf-8 -*-

from os import access
import random
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlutadeo

from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class Acciones(BaseAcciones):
    def primerapagina(self, cedula):
        try:
            self.ir(urlutadeo)
            self.sleep(2)
            
        except:
            self.salir()
            return False

        xpathInputcedula = (By.ID,"documentoIdentidad")
        xpathInputconfirmarcedula=(By.ID,"confirmaDocumentoIdentidad")
        xpathBotonContinuar=(By.XPATH,"/html/body/div[3]/form/div/input")

        visibleInputCedula = self.explicitWaitElementoVisibility(15,xpathInputcedula)
        if visibleInputCedula:
            self.escribir(xpathInputcedula,cedula)
            visibleInputConfirmarCedula = self.explicitWaitElementoVisibility(15,xpathInputconfirmarcedula)
            if visibleInputConfirmarCedula:
                self.escribir(xpathInputconfirmarcedula,cedula)
                time.sleep(1)
                self.click(xpathBotonContinuar)
 
    def segundapagina(self):
        time.sleep(3)                            
        xpathconvocatoria = (By.ID, 'convocatoria')
        xpathSIGUIENTE = (By.NAME, 'btnSiguiente')

        time.sleep(3)
        visibleonvocatoria= self.explicitWaitElementoVisibility(15,xpathconvocatoria)
        if visibleonvocatoria:
            select_element=self.findElement(xpathconvocatoria)
            select_object= Select(select_element)
            select_object.select_by_value('2022-1A - 33')
        
        self.click(xpathSIGUIENTE)

        time.sleep(5)

    def tercerapagina(self,diaExp,mesExp,anioExp,diaNac,mesNac,anionaci,NOMBRE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,sexasp,EMAIL,telefonofijo,telefonomivil):
        time.sleep(4)                            
        xpathdiaExp= (By.ID, 'diaExp')
        select_element=self.findElement(xpathdiaExp)
        select_object= Select(select_element)
        select_object.select_by_value(diaExp)
        time.sleep(1)

        time.sleep(1)                            
        xpathmesExp= (By.NAME, 'mesExp')
        select_element=self.findElement(xpathmesExp)
        select_object= Select(select_element)
        select_object.select_by_value(mesExp)
        time.sleep(1)

        time.sleep(1)
        xpathanioExp= (By.ID, 'anioExp')
        self.click(xpathanioExp)
        time.sleep(1)
        self.borrar(xpathanioExp)
        self.escribir(xpathanioExp,anioExp)
        time.sleep(1)
        
        time.sleep(1)                            
        xpathnombre= (By.NAME, 'datosBasicos.aspirante.nombre')
        self.escribir(xpathnombre,NOMBRE)
        time.sleep(1)

        time.sleep(1)                            
        xpathprimerapellido= (By.XPATH, '//*[@id="capaFormulario"]/form/div[1]/div/div[3]/table/tbody/tr[5]/td[2]/input')
        self.escribir(xpathprimerapellido,PRIMERAPELLIDO)
        time.sleep(1)        

        time.sleep(1)                            
        xpathsegundoapellido= (By.XPATH, '//*[@id="capaFormulario"]/form/div[1]/div/div[3]/table/tbody/tr[6]/td[2]/input')
        self.escribir(xpathsegundoapellido,SEGUNDOAPELLIDO)
        time.sleep(1)           

        if sexasp=="H":
            xpathHOMBRE= (By.CSS_SELECTOR, "input[type='radio'][value='H']")
            self.click(xpathHOMBRE)
        elif sexasp=="D":
            xpathMUJER= (By.CSS_SELECTOR, "input[type='radio'][value='D']")
            self.click(xpathMUJER)

        time.sleep(1)                            
        xpathdiaNac= (By.ID, 'diaNac')
        select_element=self.findElement(xpathdiaNac)
        select_object= Select(select_element)
        select_object.select_by_value(diaNac)
        time.sleep(1)            

        time.sleep(1)                            
        xpathmesNac= (By.ID, 'mesNac')
        select_element=self.findElement(xpathmesNac)
        select_object= Select(select_element)
        select_object.select_by_value(mesNac)
        time.sleep(1)           

        time.sleep(1)

        xpathanacimi= (By.ID, 'anioNac')
        self.click(xpathanacimi)
        self.borrar(xpathanacimi)
        self.escribir(xpathanacimi,anionaci)
        time.sleep(1)        

        time.sleep(3)                            
        xpathidPaissNac= (By.ID, 'idPaissNac')
        select_element=self.findElement(xpathidPaissNac)
        select_object= Select(select_element)
        select_object.select_by_value("170")
        time.sleep(1)  


        time.sleep(3)                            
        xpathiddepartanacimi= (By.NAME, 'datosBasicos.aspirante.codProvinciaNacimiento')
        select_element=self.findElement(xpathiddepartanacimi)
        select_object= Select(select_element)
        select_object.select_by_value("11")
        time.sleep(3)  


        time.sleep(5)                            
        xpathiddepartanacimi= (By.NAME, 'datosBasicos.aspirante.codMunicipioNacimiento')
        select_element=self.findElement(xpathiddepartanacimi)
        select_object= Select(select_element)
        select_object.select_by_value("1")
        time.sleep(1)  



        time.sleep(5)                            
        xpathidProvinciaNac= (By.NAME, 'datosBasicos.aspirante.domicilioCurso.codProvincia')
        select_element=self.findElement(xpathidProvinciaNac)
        select_object= Select(select_element)
        select_object.select_by_value("11")
        time.sleep(1) 


        time.sleep(5)                            
        xpathidLocalidadCur =(By.NAME, 'datosBasicos.aspirante.domicilioCurso.codLocalidad')
        select_element=self.findElement(xpathidLocalidadCur)
        select_object= Select(select_element)
        select_object.select_by_value("1")
        time.sleep(1) 

        time.sleep(1)                            
        xpathtelefonofijo= (By.NAME, 'datosBasicos.aspirante.domicilioCurso.telefono')
        self.escribir(xpathtelefonofijo,telefonofijo)
        time.sleep(1)  

        time.sleep(1)                            
        xpathtelefonomivil= (By.NAME, 'datosBasicos.aspirante.telefonoMovil')
        self.escribir(xpathtelefonomivil,telefonomivil)
        time.sleep(1)          

        time.sleep(1)                            
        xpathemail= (By.NAME, 'datosBasicos.aspirante.email')
        self.escribir(xpathemail,EMAIL)
        time.sleep(1)                  

        time.sleep(1)                            
        xpathConfirmaremail= (By.NAME, 'datosBasicos.aspirante.confirmacionEmail')
        self.escribir(xpathConfirmaremail,EMAIL)
        time.sleep(1)                  

        colegios= ["COLEGIO ACACIA II", "COLEGIO AGUAS CLARAS", "COLEGIO AGUSTIN FERNANDEZ","COLEGIO AGUSTINIANO TAGASTE", "COLEGIO ALBERTO LLERAS CAMARGO",  "COLEGIO ALDEMAR ROJAS", "COLEGIO ALEJANDRO MAGNO",
         "COLEGIO ALEJANDRO MAGNO", "COLEGIO ALEJANDRO MAGNO", "COLEGIO ALEJANDRO OBREGON","COLEGIO ALEMANIA SOLIDARIA", "COLEGIO ALEMANIA UNIFICADA","COLEGIO ALEXANDER FLEMING","COLEGIO ALFONSO LOPEZ MICHELSEN","COLEGIO ALFONSO LOPEZ PUMAREJO",
         "COLEGIO ALFONSO REYES ECHANDIA","COLEGIO ALFRED MARSHALL","COLEGIO ALFREDO IRIARTE","COLEGIO ALMIRANTE PADILLA","COLEGIO ALQUERIA DE LA FRAGUA","COLEGIO ALTAMIRA SURORIENTAL",
         "COLEGIO ALVARO GOMEZ HURTADO","COLEGIO AMANECER DE LUCES","COLEGIO ANDRES BELLO","COLEGIO ANEXO SAN FRANCISCO DE ASIS","COLEGIO ANIBAL FERNANDEZ DE SOTO","COLEGIO ANTONIO BARAYA","COLEGIO ANTONIO GRANADOS","COLEGIO ANTONIO JOSE DE SUCRE",
         "COLEGIO ANTONIO JOSE URIBE","COLEGIO ANTONIO NARIÑO","COLEGIO ANTONIO VAN UDEN","COLEGIO ANTONIO VILLAVICENCIO","COLEGIO AQUILEO PARRA","COLEGIO ARBORIZADORA ALTA","COLEGIO ARBORIZADORA BAJA",
         "COLEGIO ATAHUALPA","COLEGIO ATANASIO GIRARDOT","COLEGIO ATENAS","COLEGIO AULAS COLOMBIANAS SAN LUIS","COLEGIO AUSTRALIANO CAMPESTRE","COLEGIO AVE MARIA"]
        colegiosrd=random.choice(colegios)
        time.sleep(1)                            
        xpathColegio= (By.ID, 'idCentroEscolarExt')
        self.escribir(xpathColegio,colegiosrd)
        time.sleep(1)  

        time.sleep(1)                            
        xpathidondesentero=(By.NAME, 'datosBasicos.aspirante.tipoPromocion')
        select_element=self.findElement(xpathidondesentero)
        select_object= Select(select_element)
        select_object.select_by_value("18")
        time.sleep(1) 
        
        time.sleep(1) 
        xpathaceptardatos= (By.ID, "idPermiteDivulgarDatos")
        self.click(xpathaceptardatos)        
        time.sleep(1)         

        programaacedemicos=["P009","P010","P011","P012","P013","P014","P015","P016","P017","P018","P019"]
        programaacad=random.choice(programaacedemicos)

        time.sleep(2)                            
        xpathprogramaacademico=(By.NAME, 'datosBasicos.aspirante.plan')
        select_element=self.findElement(xpathprogramaacademico)
        select_object= Select(select_element)
        select_object.select_by_value(programaacad)
        time.sleep(5) 

        time.sleep(1)                            
        try:  
            xpathcentroplan=(By.ID, 'centroPlan')
            select_element=self.findElement(xpathcentroplan)
            select_object= Select(select_element)
            select_object.select_by_value("10")
            time.sleep(1)         
        except:
            time.sleep(2) 
            xpathcentroplan=(By.ID, 'centroPlan')
            select_element=self.findElement(xpathcentroplan)
            select_object= Select(select_element)
            select_object.select_by_value("10")
            
        time.sleep(5)
        try:                            
            xpathcriterioCentroPlan=(By.NAME, 'datosBasicos.aspirante.criterio')
            select_element=self.findElement(xpathcriterioCentroPlan)
            select_object= Select(select_element)
            select_object.select_by_value("CRU")
            time.sleep(2)   
        except:
            time.sleep(2)   
            xpathcriterioCentroPlan=(By.NAME, 'datosBasicos.aspirante.criterio')
            select_element=self.findElement(xpathcriterioCentroPlan)
            select_object= Select(select_element)
            select_object.select_by_value("CRU")


        xpathbtnSiguiente=(By.XPATH, '//*[@id="capaFormulario"]/div[4]/input')
        self.click(xpathbtnSiguiente)
        print ("boton siguiente final")
        time.sleep(20)
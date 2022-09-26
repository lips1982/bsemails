# -*- coding: utf-8 -*-
import time
from PQTs.Selenium.Base import BaseAcciones

from PQTs.Utilizar import urlutadeo ,urlloginemail

from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
import subprocess
import sys
import time

class Acciones(BaseAcciones):

    def paginacero(self, usuario):
        try:
            self.ir('https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')
            self.sleep(2)
        except:
            self.salir()
            return False

        xpathgmailidentifierId = (By.ID,"identifierId")
        visiblealternativeEmail = self.explicitWaitElementoVisibility(15,xpathgmailidentifierId)
        if visiblealternativeEmail:
                self.escribir(xpathgmailidentifierId,f"{usuario}@utadeo.edu.co")
                self.enter(xpathgmailidentifierId)
                time.sleep(2)



        time.sleep(3)
    def primerapagina(self, usuario, password):
        try:
            self.ir(urlloginemail)
            self.sleep(2)
            
        except:
            self.salir()
            return False

        xpathusername = (By.ID,"username")
        xpathpassword=(By.ID,"password")
        xpathbotoninicio=(By.CLASS_NAME,"btn-primary")


        visibleUsuario = self.explicitWaitElementoVisibility(15,xpathusername)
        if visibleUsuario:
            self.escribir(xpathusername,usuario)
            visiblePassword = self.explicitWaitElementoVisibility(15,xpathpassword)
            if visiblePassword:
                self.escribir(xpathpassword,password)
                time.sleep(2)
                visibleBoton = self.explicitWaitElementoVisibility(15,xpathbotoninicio)
                if visibleBoton:
                    self.click(xpathbotoninicio)
                    time.sleep(2)
        time.sleep(3)
    
    def segundapagina(self,EMAILRECUPERACION,RESPUESTA,usuario,PASSWORD):

        xpathalternativeEmail = (By.ID,"alternativeEmail")
        xpathpreguntarecuperacion=(By.ID,"password")
        xpathbotoninicio=(By.CLASS_NAME,"btn-primary")
        
        visiblealternativeEmail = self.explicitWaitElementoVisibility(15,xpathalternativeEmail)
        if visiblealternativeEmail:
            self.escribir(xpathalternativeEmail,EMAILRECUPERACION)
        else:
            self.ir('https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')
            time.sleep(3)
            xpathgmailidentifierId = (By.ID,"identifierId")
            xpathbotoninicio=(By.CLASS_NAME,"btn-primary")
            visiblealternativeEmail = self.explicitWaitElementoVisibility(15,xpathgmailidentifierId)
            if visiblealternativeEmail:
                self.escribir(xpathgmailidentifierId,f"{usuario}@utadeo.edu.co")
                self.enter(xpathgmailidentifierId)
                time.sleep(2)

                self.ir(urlloginemail)
                self.sleep(2)

                xpathusername = (By.ID,"username")
                xpathpassword=(By.ID,"password")
                

                visibleUsuario = self.explicitWaitElementoVisibility(15,xpathusername)
                if visibleUsuario:
                    self.escribir(xpathusername,usuario)
                    visiblePassword = self.explicitWaitElementoVisibility(10,xpathpassword)
                    if visiblePassword:
                        self.escribir(xpathpassword,PASSWORD)
                        time.sleep(2)
                        visiblebotoninicio= self.explicitWaitElementoVisibility(10,xpathbotoninicio)
                        if visiblebotoninicio:
                            self.click(xpathbotoninicio)
                            time.sleep(2)

                time.sleep(2)

        xpathpreguntarecuperacion = (By.ID, 'questionMenu')
        visiblepreguntarecuperacion = self.explicitWaitElementoVisibility(15,xpathpreguntarecuperacion)
        if visiblepreguntarecuperacion:
            select_element=self.findElement(xpathpreguntarecuperacion)
            select_object= Select(select_element)
            select_object.select_by_value('¿Cuál es el nombre de su mascota?')
            time.sleep(1)
         
        xpathsecretAnswer = (By.ID,"secretAnswer") 
        visiblesecretAnswer= self.explicitWaitElementoVisibility(15,xpathsecretAnswer)
        if visiblesecretAnswer:
            self.escribir(xpathsecretAnswer,RESPUESTA)
            time.sleep(1)
            self.enter(xpathsecretAnswer)

        xpathgoogleconfirm = (By.ID,"confirm") 
        visiblegoogleconfirm = self.explicitWaitElementoVisibility(30,xpathgoogleconfirm)
        if visiblegoogleconfirm:
            self.click(xpathgoogleconfirm)
        
        time.sleep(5)
        self.refreshweb()
        time.sleep(5)

    def capture_and_echo_stdout(self,cmd,cmd2):
        """ Start a subprocess and write its stdout to stdout of this process.     
        Capture and return stdout lines as a list. """
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        time.sleep(60)
        proc = subprocess.Popen(cmd2, stdout=subprocess.PIPE)
        
        if proc.returncode:
            raise subprocess.CalledProcessError(proc.returncode, cmd)

    def paginasologmailscuentas(self, usuario,password):
        try:
            self.ir('https://gmail.com')
            self.sleep(2)
        except:
            self.salir()
            return False

        xpathgmailidentifierId = (By.ID,"identifierId")
        xpathgsiguiente= (By.CLASS_NAME,"Passwd")

        xpathgmailpassword = (By.NAME,"VfPpkd-vQzf8d")
        
        visiblealternativeEmail = self.explicitWaitElementoVisibility(15,xpathgmailidentifierId)
        if visiblealternativeEmail:
            self.escribir(xpathgmailidentifierId,usuario)
            self.enter(xpathgmailidentifierId)
            time.sleep(2)
            visiblesiguiente = self.explicitWaitElementoVisibility(15,xpathgsiguiente)
            if visiblesiguiente:
                self.click(xpathgsiguiente)
                time.sleep(2)            
            
                visiblegmailpassword = self.explicitWaitElementoVisibility(30,xpathgmailpassword)


                if visiblegmailpassword:
                    self.escribir(xpathgmailpassword,password)
                    self.enter(xpathgmailpassword)
                    time.sleep(2)


        time.sleep(30)

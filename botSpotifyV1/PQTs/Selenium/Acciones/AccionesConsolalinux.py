import os
import subprocess
import sys
import time

 


def capture_and_echo_stdout():

    cmdIpRoute = 'gcloud auth login'
    ejecutarProceso = subprocess.Popen(cmdIpRoute, stdout=subprocess.PIPE, shell=True)
    
    linklogin = ejecutarProceso.communicate()[1].decode('utf-8').strip()
    f = open('gcloud.txt','w')
    f.write(str(linklogin))
    f.close()
    print(linklogin)

capture_and_echo_stdout()
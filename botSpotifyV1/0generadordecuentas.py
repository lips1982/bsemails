#str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

#DATOS1001={"cedula":"506910995", "NOMBRE":"OLGA", "PRIMERAPELLIDO":"ZURA","SEGUNDOAPELLIDO":"OROZCO","sexasp":"D","EMAIL":"anferneeqkimora@slgmail.tk"}

from dataclasses import replace
import random
import string
from PQTs.Utilizar import listaapellidos, listanombresexo
def getRandomString(length):
    pool=string.ascii_lowercase+string.digits
    return ''.join(random.choice(pool) for i in range(length))

for i in range(0,10000) :

    
    cedula =random.randint(1000000,10000000)
    nombresexo=random.choice(listanombresexo)
    apellido1 =random.choice(listaapellidos)
    apellido2 =random.choice(listaapellidos)
    usuario=getRandomString(14)
    email =f'{usuario}@slgmail.tk' 
    dato=f'DATOS{i}= $ "item":{i}, "cedula":"{cedula}", "NOMBRE":"{nombresexo["nombre"]}", "PRIMERAPELLIDO":"{apellido1}","SEGUNDOAPELLIDO":"{apellido2}","sexasp":"{nombresexo["sexo"]}","USUARIO":"{usuario}","EMAIL":"{email}"%'
    dato=dato.replace("$","{")
    dato=dato.replace("%","}")
    with open("DATOSCUENTAS.txt", "a") as f:
        f.write(f"{dato}\n")
        f.close()  
    with open("DATOSSOLOEMAIL.txt", "a") as f:
        f.write(f"{email},!asdf2022,100\n")
        f.close()      
                                   
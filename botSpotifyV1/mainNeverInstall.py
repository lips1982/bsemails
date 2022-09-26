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
    listaa=[4	,
5	,
7	,
12	,
13	,
18	,
19	,
20	,
23	,
37	,
40	,
41	,
44	,
46	,
48	,
51	,
54	,
64	,
70	,
74	,
79	,
82	,
86	,
89	,
95	,
99	,
101	,
108	,
109	,
111	,
112	,
113	,
116	,
125	,
129	,
130	,
133	,
137	,
149	,
151	,
162	,
164	,
169	,
173	,
174	,
175	,
178	,
179	,
180	,
182	,
183	,
184	,
188	,
192	,
193	,
194	,
195	,
197	,
198	,
202	,
203	,
204	,
210	,
212	,
213	,
218	,
225	,
231	,
237	,
238	,
246	,
248	,
252	,
253	,
256	,
259	,
262	,
271	,
274	,
276	,
282	,
286	,
289	,
292	,
294	,
299	,
303	,
308	,
310	,
312	,
316	,
319	,
321	,
323	,
329	,
330	,
336	,
337	,
342	,
345	,
346	,
359	,
360	,
367	,
368	,
372	,
373	,
375	,
387	,
401	,
403	,
404	,
413	,
415	,
417	,
419	,
420	,
422	,
428	,
434	,
445	,
446	,
448	,
452	,
473	,
474	,
477	,
479	,
480	,
481	,
486	,
487	,
502	,
503	,
505	,
506	,
509	,
531	,
532	,
535	,
542	,
543	,
565	,
569	,
572	,
579	,
582	,
587	,
589	,
593	,
595	,
599	,
601	,
608	,
619	,
624	,
625	,
637	,
638	,
639	,
640	,
646	,
651	,
655	,
658	,
662	,
664	,
669	,
675	,
691	,
692	,
695	,
698	,
700	,
707	,
709	,
710	,
713	,
719	,
724	,
726	,
730	,
731	,
735	,
738	,
741	,
742	,
743	,
747	,
752	,
755	,
758	,
759	,
760	,
763	,
766	,
777	,
784	,
787	,
790	,
791	,
792	,
795	,
801	,
804	,
812	,
823	,
824	,
835	,
847	,
848	,
849	,
856	,
870	,
871	,
883	,
885	,
886	,
888	,
890	,
892	,
893	,
900	,
907	,
912	,
913	,
914	,
920	,
924	,
937	,
943	,
954	,
957	,
958	,
959	,
963	,
965	,
968	,
970	,
974	,
975	,
982	,
985	,
990	,
995	,
997	,
999	,
1002	,
1008	,
1009	,
1010	,
1011	,
1018	,
1020	,
1023	,
1024	,
1026	,
1029	,
1039	,
1040	,
1042	,
1043	,
1054	,
1065	,
1069	,
1070	,
1079	,
1082	,
1084	,
1087	,
1093	,
1103	,
1108	,
1119	,
1123	,
1127	,
1141	,
1145	,
1146	,
1152	,
1156	,
1157	,
1161	,
1165	,
1166	,
1170	,
1173	,
1176	,
1177	,
1180	,
1184	,
1187	,
1196	,
1203	,
1207	,
1210	,
1218	,
1226	,
1232	,
1234	,

]
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






# -*- coding: utf-8 -*-
#TESTTTTT

import random
from PQTs.MongoDB.MongoDB import MongoDB
from PQTs.Selenium.Base import BaseConexion
from PQTs.Selenium.Acciones.AccionesloginEmail import Acciones
from threading import Thread, Barrier
import time
from vpn import Windscribe

hilos=1
start= time.time()


def iniciarbot(USUARIO,PASSWORD,EMAILRECUPERACION,RESPUESTA):

    driver = BaseConexion().conexionChrome()
    #driver = BaseConexion().conexionChromeHeadless()

    acciones = Acciones(driver)
    acciones.paginacero(USUARIO)
    acciones.primerapagina(USUARIO,PASSWORD)

    acciones.segundapagina(EMAILRECUPERACION,RESPUESTA,USUARIO,PASSWORD)
    cmd1 = ["gcloud", "auth", "login"]
    cmd2 = ["python3", "bot.py"]

    acciones.capture_and_echo_stdout(cmd1,cmd2)
    time.sleep(50)
DATOS1={"USUARIO":"maria.plazag", "PASSWORD":"34554264", "EMAILRECUPERACION":"yandelqjayden@slgmail.tk"}
DATOS2={"USUARIO":"maria.mirandaj", "PASSWORD":"34534001", "EMAILRECUPERACION":"kiarakxneytiri@slgmail.tk"}
DATOS3={"USUARIO":"maria.figueroag", "PASSWORD":"34555659", "EMAILRECUPERACION":"anferneehrhayden@slgmail.tk"}
DATOS4={"USUARIO":"maria.casasf", "PASSWORD":"34538323", "EMAILRECUPERACION":"yarelyshtanairi@slgmail.tk"}
DATOS5={"USUARIO":"maria.bendeckl", "PASSWORD":"41573309", "EMAILRECUPERACION":"evoletzcyandel@slgmail.tk"}
DATOS6={"USUARIO":"marta.ochoac", "PASSWORD":"34530003", "EMAILRECUPERACION":"shainajvvalerie@slgmail.tk"}
DATOS7={"USUARIO":"marta.palominom", "PASSWORD":"34547349", "EMAILRECUPERACION":"danitzaufcheyenne@slgmail.tk"}
DATOS8={"USUARIO":"maria.canencios", "PASSWORD":"34558215", "EMAILRECUPERACION":"evoletsvshanaya@slgmail.tk"}
DATOS9={"USUARIO":"marta.chaguendod", "PASSWORD":"34558810", "EMAILRECUPERACION":"daniraecilma@slgmail.tk"}
DATOS10={"USUARIO":"mario.lopezp", "PASSWORD":"10528527", "EMAILRECUPERACION":"samaryqyumalay@slgmail.tk"}
DATOS11={"USUARIO":"marlem.mariacam", "PASSWORD":"34542432", "EMAILRECUPERACION":"sharlotteppshanaya@slgmail.tk"}
DATOS12={"USUARIO":"maria.velascos", "PASSWORD":"34542310", "EMAILRECUPERACION":"valeriezuamara@slgmail.tk"}
DATOS13={"USUARIO":"mario.valenciac", "PASSWORD":"10285254", "EMAILRECUPERACION":"crisbellibkenisha@slgmail.tk"}
DATOS14={"USUARIO":"marisol.jordanm", "PASSWORD":"34560136", "EMAILRECUPERACION":"ohanaahsharlotte@slgmail.tk"}
DATOS15={"USUARIO":"mario.lassoo", "PASSWORD":"10528987", "EMAILRECUPERACION":"evoletqyarely@slgmail.tk"}
DATOS16={"USUARIO":"m.rodriguez", "PASSWORD":"34541655", "EMAILRECUPERACION":"danitzaebohana@slgmail.tk"}
DATOS17={"USUARIO":"maria.alvarezv", "PASSWORD":"41733718", "EMAILRECUPERACION":"anakinqskerlin@slgmail.tk"}
DATOS18={"USUARIO":"maria.astudillop", "PASSWORD":"34562778", "EMAILRECUPERACION":"crisbelltfyaritza@slgmail.tk"}
DATOS19={"USUARIO":"maricela.munozl", "PASSWORD":"34530973", "EMAILRECUPERACION":"amaruvnnovalee@slgmail.tk"}
DATOS20={"USUARIO":"maritza.lopezg", "PASSWORD":"48600362", "EMAILRECUPERACION":"anakindkvalerie@slgmail.tk"}
DATOS21={"USUARIO":"marisol.munozo", "PASSWORD":"34569042", "EMAILRECUPERACION":"jailenexodanira@slgmail.tk"}
DATOS22={"USUARIO":"martha.pasquelr", "PASSWORD":"34551101", "EMAILRECUPERACION":"shanayapskiara@slgmail.tk"}
DATOS23={"USUARIO":"mauro.egasr", "PASSWORD":"12991300", "EMAILRECUPERACION":"sharlotteihilma@slgmail.tk"}
DATOS24={"USUARIO":"miguel.fallag", "PASSWORD":"76306235", "EMAILRECUPERACION":"kenishavharizona@slgmail.tk"}
DATOS25={"USUARIO":"martha.vivasc", "PASSWORD":"34544390", "EMAILRECUPERACION":"samaryutamaru@slgmail.tk"}
DATOS26={"USUARIO":"martha.arevalos", "PASSWORD":"25611423", "EMAILRECUPERACION":"julissayhhayden@slgmail.tk"}
DATOS27={"USUARIO":"martha.cortezb", "PASSWORD":"34552524", "EMAILRECUPERACION":"crisbellwumaiara@slgmail.tk"}
DATOS28={"USUARIO":"martha.herrerac", "PASSWORD":"31289152", "EMAILRECUPERACION":"jazzlynzyjailene@slgmail.tk"}
DATOS29={"USUARIO":"mendoza.martha", "PASSWORD":"51599545", "EMAILRECUPERACION":"anakinsrlindsay@slgmail.tk"}
DATOS30={"USUARIO":"mary.alzatec", "PASSWORD":"34538776", "EMAILRECUPERACION":"shadypvcheyenne@slgmail.tk"}
DATOS31={"USUARIO":"mauricio.orozcoc", "PASSWORD":"76326581", "EMAILRECUPERACION":"leanneassamary@slgmail.tk"}
DATOS32={"USUARIO":"miller.garciaz", "PASSWORD":"10538660", "EMAILRECUPERACION":"anferneeaayanet@slgmail.tk"}
DATOS33={"USUARIO":"miguel.corchuelom", "PASSWORD":"19427110", "EMAILRECUPERACION":"ilmatileanne@slgmail.tk"}
DATOS34={"USUARIO":"martha.bolivarl", "PASSWORD":"45766496", "EMAILRECUPERACION":"anferneemamaiara@slgmail.tk"}
DATOS35={"USUARIO":"martha.mendozab", "PASSWORD":"63483237", "EMAILRECUPERACION":"yaritzahimaiara@slgmail.tk"}
DATOS36={"USUARIO":"mauricio.mellizor", "PASSWORD":"10521309", "EMAILRECUPERACION":"anferneespyaneli@slgmail.tk"}
DATOS37={"USUARIO":"mary.gahonal", "PASSWORD":"34555766", "EMAILRECUPERACION":"arizonaiemaiara@slgmail.tk"}
DATOS38={"USUARIO":"miguel.piedrahitag", "PASSWORD":"46166170", "EMAILRECUPERACION":"yumalayukyarely@slgmail.tk"}
DATOS39={"USUARIO":"miguel.ninoz", "PASSWORD":"91288035", "EMAILRECUPERACION":"valeriezbjazzlyn@slgmail.tk"}
DATOS40={"USUARIO":"meydee.perezd", "PASSWORD":"34528225", "EMAILRECUPERACION":"danitzayhlindsay@slgmail.tk"}
DATOS41={"USUARIO":"milton.lopezg", "PASSWORD":"76307943", "EMAILRECUPERACION":"yumalayaoanfernee@slgmail.tk"}
DATOS42={"USUARIO":"milton.diazm", "PASSWORD":"76321456", "EMAILRECUPERACION":"kenaihvcrisbell@slgmail.tk"}
DATOS43={"USUARIO":"milton.arangoq", "PASSWORD":"79390100", "EMAILRECUPERACION":"yanellihiyarely@slgmail.tk"}
DATOS44={"USUARIO":"mirtha.espinosau", "PASSWORD":"27450864", "EMAILRECUPERACION":"maiarayijazzlyn@slgmail.tk"}
DATOS45={"USUARIO":"mirta.olavel", "PASSWORD":"34537470", "EMAILRECUPERACION":"dexterzqjailene@slgmail.tk"}
DATOS46={"USUARIO":"miryam.torresl", "PASSWORD":"29881316", "EMAILRECUPERACION":"shanayailvalerie@slgmail.tk"}
DATOS47={"USUARIO":"miryam.bustosv", "PASSWORD":"34320823", "EMAILRECUPERACION":"anakinlnshady@slgmail.tk"}
DATOS48={"USUARIO":"miryam.garciaz", "PASSWORD":"34534976", "EMAILRECUPERACION":"jackieipanfernee@slgmail.tk"}
DATOS49={"USUARIO":"miguel.idrobos", "PASSWORD":"34531063", "EMAILRECUPERACION":"neytiriynanfernee@slgmail.tk"}
DATOS50={"USUARIO":"monica.bucheliq", "PASSWORD":"34570500", "EMAILRECUPERACION":"kerlinlskimora@slgmail.tk"}
DATOS51={"USUARIO":"miguel.insuastiv", "PASSWORD":"34529212", "EMAILRECUPERACION":"sharlottehbarizona@slgmail.tk"}
DATOS52={"USUARIO":"misael.morcilloc", "PASSWORD":"76303530", "EMAILRECUPERACION":"anakinlfvalerie@slgmail.tk"}
DATOS53={"USUARIO":"miller.orozcop", "PASSWORD":"34528351", "EMAILRECUPERACION":"anferneexnyaritza@slgmail.tk"}
DATOS54={"USUARIO":"moises.hernandeza", "PASSWORD":"10540346", "EMAILRECUPERACION":"ohanajbnovalee@slgmail.tk"}
DATOS55={"USUARIO":"miller.valdezs", "PASSWORD":"34527012", "EMAILRECUPERACION":"yumalayfnamaru@slgmail.tk"}
DATOS56={"USUARIO":"miyer.murilloa", "PASSWORD":"76314294", "EMAILRECUPERACION":"maverickacheyenne@slgmail.tk"}
DATOS57={"USUARIO":"myriam.panchoagac", "PASSWORD":"25271533", "EMAILRECUPERACION":"valerievrdexter@slgmail.tk"}
DATOS58={"USUARIO":"nancy.lopezr", "PASSWORD":"34537406", "EMAILRECUPERACION":"yaritzaiushaina@slgmail.tk"}
DATOS59={"USUARIO":"nancy.fernandeza", "PASSWORD":"25637641", "EMAILRECUPERACION":"haydenuoneytiri@slgmail.tk"}
DATOS60={"USUARIO":"myriam.hernandezr", "PASSWORD":"34528792", "EMAILRECUPERACION":"sherlynefkenisha@slgmail.tk"}
DATOS61={"USUARIO":"napoleon.zambranoa", "PASSWORD":"16342484", "EMAILRECUPERACION":"shadyqevalerie@slgmail.tk"}
DATOS62={"USUARIO":"nelson.gomezh", "PASSWORD":"10533819", "EMAILRECUPERACION":"kenishalishaina@slgmail.tk"}
DATOS63={"USUARIO":"olga.valdesc", "PASSWORD":"34539672", "EMAILRECUPERACION":"sherlynprhayden@slgmail.tk"}
DATOS64={"USUARIO":"olga.certuchem", "PASSWORD":"34557739", "EMAILRECUPERACION":"yanellicaleanne@slgmail.tk"}
DATOS65={"USUARIO":"olga.cadenad", "PASSWORD":"52021928", "EMAILRECUPERACION":"crisbellllohana@slgmail.tk"}
DATOS66={"USUARIO":"oscar.bermudezc", "PASSWORD":"67609430", "EMAILRECUPERACION":"leanneqsyanelli@slgmail.tk"}
DATOS67={"USUARIO":"oscar.vivasa", "PASSWORD":"10548134", "EMAILRECUPERACION":"yandelemlindsay@slgmail.tk"}
DATOS68={"USUARIO":"oscar.riosr", "PASSWORD":"65583970", "EMAILRECUPERACION":"arizonaeeyarely@slgmail.tk"}
DATOS69={"USUARIO":"g-orlando", "PASSWORD":"16627961", "EMAILRECUPERACION":"danitzaecnovalee@slgmail.tk"}
DATOS70={"USUARIO":"oscar.munoza", "PASSWORD":"10538031", "EMAILRECUPERACION":"jailenelzanfernee@slgmail.tk"}
DATOS71={"USUARIO":"olga.paredesm", "PASSWORD":"34533114", "EMAILRECUPERACION":"evoletwvarizona@slgmail.tk"}
DATOS72={"USUARIO":"noira.rualesc", "PASSWORD":"34537521", "EMAILRECUPERACION":"amaracqjailene@slgmail.tk"}
DATOS73={"USUARIO":"nelson.rivasb", "PASSWORD":"10537188", "EMAILRECUPERACION":"kenishaqvmaverick@slgmail.tk"}
DATOS74={"USUARIO":"olga.hoyoss", "PASSWORD":"31948475", "EMAILRECUPERACION":"samarylxvalerie@slgmail.tk"}
DATOS75={"USUARIO":"ordonez.vallecillav", "PASSWORD":"34533437", "EMAILRECUPERACION":"yaneliopdanira@slgmail.tk"}
DATOS76={"USUARIO":"nubia.urreah", "PASSWORD":"34544841", "EMAILRECUPERACION":"jackievodexter@slgmail.tk"}
DATOS77={"USUARIO":"olga.camachom", "PASSWORD":"34549510", "EMAILRECUPERACION":"dextercasherlyn@slgmail.tk"}
DATOS78={"USUARIO":"orlando.gutierrezj", "PASSWORD":"10539208", "EMAILRECUPERACION":"amarabwnovalee@slgmail.tk"}
DATOS79={"USUARIO":"nestor.velascov", "PASSWORD":"10544063", "EMAILRECUPERACION":"jazzlynywshaina@slgmail.tk"}
DATOS80={"USUARIO":"olga.paredesc", "PASSWORD":"34529748", "EMAILRECUPERACION":"lindsaysskiara@slgmail.tk"}
DATOS81={"USUARIO":"nhora.herreral", "PASSWORD":"34542339", "EMAILRECUPERACION":"amarasscheyenne@slgmail.tk"}
DATOS82={"USUARIO":"nicolas.fernandezs", "PASSWORD":"10523416", "EMAILRECUPERACION":"yandelhzvalerie@slgmail.tk"}
DATOS83={"USUARIO":"noe.albanl", "PASSWORD":"10537683", "EMAILRECUPERACION":"amarucwjulissa@slgmail.tk"}
DATOS84={"USUARIO":"nidia.satizabalc", "PASSWORD":"25270727", "EMAILRECUPERACION":"jailenepvkimora@slgmail.tk"}
DATOS85={"USUARIO":"oscar.orozcoo", "PASSWORD":"10522279", "EMAILRECUPERACION":"kenaipyyarely@slgmail.tk"}
DATOS86={"USUARIO":"omar.hincapier", "PASSWORD":"10547914", "EMAILRECUPERACION":"maverickavjazzlyn@slgmail.tk"}
DATOS87={"USUARIO":"nidia.menesesm", "PASSWORD":"26566163", "EMAILRECUPERACION":"tanairimvshanaya@slgmail.tk"}
DATOS88={"USUARIO":"nubia.oliverosc", "PASSWORD":"41736871", "EMAILRECUPERACION":"yanetqvjackie@slgmail.tk"}
DATOS89={"USUARIO":"orlando.rodriguezb", "PASSWORD":"10528196", "EMAILRECUPERACION":"evoletuhtanairi@slgmail.tk"}
DATOS90={"USUARIO":"oscar.camayov", "PASSWORD":"76332255", "EMAILRECUPERACION":"evoletmvjailene@slgmail.tk"}
DATOS91={"USUARIO":"victor.rodriguezl", "PASSWORD":"76306528", "EMAILRECUPERACION":"arizonaruyaneli@slgmail.tk"}
DATOS92={"USUARIO":"zuly.novoar", "PASSWORD":"34564288", "EMAILRECUPERACION":"kiarakekimora@slgmail.tk"}
DATOS93={"USUARIO":"wilson.benavidesr", "PASSWORD":"18125465", "EMAILRECUPERACION":"kiarajnkiara@slgmail.tk"}
DATOS94={"USUARIO":"vladimir.trujilloa", "PASSWORD":"76320040", "EMAILRECUPERACION":"sherlynfbanfernee@slgmail.tk"}
DATOS95={"USUARIO":"victor.vivasr", "PASSWORD":"10526184", "EMAILRECUPERACION":"danitzajamara@slgmail.tk"}
DATOS96={"USUARIO":"yulietd.riveram", "PASSWORD":"34559928", "EMAILRECUPERACION":"amaraiwyanet@slgmail.tk"}
DATOS97={"USUARIO":"yenni.zambranol", "PASSWORD":"14965889", "EMAILRECUPERACION":"cheyennerytanairi@slgmail.tk"}
DATOS98={"USUARIO":"ximena.astudilloh", "PASSWORD":"10517940", "EMAILRECUPERACION":"shainaqesherlyn@slgmail.tk"}
DATOS99={"USUARIO":"ximena.vivash", "PASSWORD":"16711797", "EMAILRECUPERACION":"danitzavpneytiri@slgmail.tk"}
DATOS100={"USUARIO":"yolanda.burbanon", "PASSWORD":"75616350", "EMAILRECUPERACION":"kiarafhjanice@slgmail.tk"}

listadatos=[DATOS1,DATOS2,DATOS3,DATOS4,DATOS5,DATOS6,DATOS7,DATOS8,DATOS9,DATOS10,DATOS11,DATOS12,DATOS13,DATOS14,DATOS15,DATOS16,DATOS17,DATOS18,DATOS19,DATOS20,DATOS21,DATOS22,DATOS23,DATOS24,DATOS25,DATOS26,DATOS27,DATOS28,DATOS29,DATOS30,DATOS31,DATOS32,DATOS33,DATOS34,DATOS35,DATOS36,DATOS37,DATOS38,DATOS39,DATOS40,DATOS41,DATOS42,DATOS43,DATOS44,DATOS45,DATOS46,DATOS47,DATOS48,DATOS49,DATOS50,DATOS51,DATOS52,DATOS53,DATOS54,DATOS55,DATOS56,DATOS57,DATOS58,DATOS59,DATOS60,DATOS61,DATOS62,DATOS63,DATOS64,DATOS65,DATOS66,DATOS67,DATOS68,DATOS69,DATOS70,DATOS71,DATOS72,DATOS73,DATOS74,DATOS75,DATOS76,DATOS77,DATOS78,DATOS79,DATOS80,DATOS81,
DATOS82	,DATOS83	,DATOS84	,DATOS85	,DATOS86	,DATOS87	,DATOS88	,DATOS89	,DATOS90	,DATOS91	,DATOS92	,DATOS93	,DATOS94	,DATOS95	,
DATOS96	,DATOS97	,DATOS98	,DATOS99	,DATOS100]


'''DATOS80,DATOS81,DATOS82,DATOS83,DATOS84,DATOS85,DATOS86,DATOS87,DATOS88,DATOS89,DATOS90,DATOS91,DATOS92,DATOS93,DATOS94,DATOS95,DATOS96,DATOS97,DATOS98,DATOS99,DATOS100,DATOS101,DATOS102,DATOS103,DATOS104,DATOS105,DATOS106,DATOS107,DATOS108,DATOS109,DATOS110,DATOS111,DATOS112,DATOS113,DATOS114,DATOS115,DATOS116,DATOS117,DATOS118,DATOS119,DATOS120,DATOS121,DATOS122,DATOS123,DATOS124,DATOS125,DATOS126,
DATOS127,DATOS128,DATOS129,DATOS130,DATOS131,DATOS132,DATOS133,DATOS134,DATOS135,DATOS136,DATOS137,DATOS138,DATOS139,DATOS140,DATOS141,DATOS142,DATOS143,DATOS144,DATOS145,DATOS146,DATOS147,DATOS148,DATOS149,DATOS150,DATOS151,DATOS152,DATOS153,DATOS154,DATOS155,DATOS156,DATOS157,DATOS158,DATOS159,DATOS160,DATOS161,DATOS162,DATOS163,DATOS164,DATOS165,DATOS166,DATOS167,DATOS168,DATOS169,DATOS170,DATOS171,DATOS172,DATOS173,DATOS174,DATOS175,DATOS176,DATOS177,DATOS178,DATOS179,DATOS180,DATOS181,DATOS182,DATOS183,DATOS184,DATOS185,DATOS186,DATOS187,DATOS188,DATOS189,DATOS190,DATOS191,DATOS192,DATOS193,DATOS194,DATOS195,DATOS196,DATOS197,DATOS198,DATOS199,DATOS200,
DATOS201,DATOS202,DATOS203,DATOS204,DATOS205,DATOS206,DATOS207,DATOS208,DATOS209,DATOS210,DATOS211,DATOS212,DATOS213,DATOS214,DATOS215,DATOS216,DATOS217,DATOS218,DATOS219,DATOS220,DATOS221,DATOS222,DATOS223,DATOS224,DATOS225,DATOS226,DATOS227,DATOS228,DATOS229,DATOS230,DATOS231,DATOS232,DATOS233,DATOS234,DATOS235,DATOS236,DATOS237,DATOS238,DATOS239,DATOS240,DATOS241,DATOS242,DATOS243,DATOS244,DATOS245,DATOS246,DATOS247,DATOS248,DATOS249,DATOS250,DATOS251,DATOS252,DATOS253,DATOS254,DATOS255,DATOS256,DATOS257,DATOS258,DATOS259,DATOS260,DATOS261,DATOS262,DATOS263,DATOS264,DATOS265,DATOS266,DATOS267,DATOS268,DATOS269,DATOS270,DATOS271,DATOS272,DATOS273,DATOS274,DATOS275,DATOS276,
DATOS277,DATOS278,DATOS279,DATOS280,DATOS281,DATOS282,DATOS283,DATOS284,DATOS285,DATOS286,DATOS287,DATOS288,DATOS289,DATOS290,DATOS291,DATOS292,DATOS293,DATOS294,DATOS295,DATOS296,DATOS297,DATOS298,DATOS299,DATOS300,DATOS301,DATOS302,DATOS303,DATOS304,DATOS305,DATOS306,DATOS307,DATOS308,DATOS309,DATOS310,DATOS311,DATOS312,DATOS313,DATOS314,DATOS315,DATOS316,DATOS317,DATOS318,DATOS319,DATOS320,DATOS321,DATOS322,DATOS323,DATOS324,DATOS325,DATOS326,DATOS327,DATOS328,DATOS329,DATOS330,DATOS331,DATOS332,DATOS333,DATOS334,DATOS335,DATOS336,DATOS337,DATOS338,DATOS339,DATOS340,DATOS341,DATOS342,DATOS343,DATOS344,DATOS345,DATOS346,DATOS347,DATOS348,DATOS349,DATOS350,DATOS351,DATOS352,DATOS353,DATOS354,DATOS355,DATOS356,
DATOS357,DATOS358,DATOS359,DATOS360,DATOS361,DATOS362,DATOS363,DATOS364,DATOS365,DATOS366,DATOS367,DATOS368,DATOS369,DATOS370,DATOS371,DATOS372,DATOS373,DATOS374,DATOS375,DATOS376,DATOS377,DATOS378,DATOS379,DATOS380,DATOS381,DATOS382,DATOS383,DATOS384,DATOS385,DATOS386,DATOS387,DATOS388,DATOS389,DATOS390,DATOS391,DATOS392,DATOS393,DATOS394,DATOS395,DATOS396,DATOS397,DATOS398,DATOS399,DATOS400,DATOS401,DATOS402,DATOS403,DATOS404,DATOS405,DATOS406,DATOS407,DATOS408,DATOS409,DATOS410,DATOS411,DATOS412,DATOS413,DATOS414,DATOS415,DATOS416,DATOS417,DATOS418,DATOS419,DATOS420,DATOS421,DATOS422,DATOS423,DATOS424,DATOS425,DATOS426,DATOS427,DATOS428,DATOS429,DATOS430,DATOS431,DATOS432,DATOS433,DATOS434,DATOS435,DATOS436,DATOS437,DATOS438,
DATOS439,DATOS440,DATOS441,DATOS442,DATOS443,DATOS444,DATOS445,DATOS446,DATOS447,DATOS448,DATOS449,DATOS450,DATOS451,DATOS452,DATOS453,DATOS454,DATOS455,DATOS456,DATOS457,DATOS458,DATOS459,DATOS460,DATOS461,DATOS462,DATOS463,DATOS464,DATOS465,DATOS466,DATOS467,DATOS468,DATOS469,DATOS470,DATOS471,DATOS472,DATOS473,DATOS474,DATOS475,DATOS476,DATOS477,DATOS478,DATOS479,DATOS480,DATOS481,DATOS482,DATOS483,DATOS484,DATOS485,DATOS486,DATOS487,DATOS488,DATOS489,DATOS490,DATOS491,DATOS492,DATOS493,DATOS494,DATOS495,DATOS496,DATOS497,DATOS498,DATOS499,DATOS500,DATOS501,DATOS502,DATOS503,DATOS504,DATOS505,DATOS506,DATOS507,
DATOS508,DATOS509,DATOS510,DATOS511,DATOS512,DATOS513,DATOS514,DATOS515,DATOS516,DATOS517,DATOS518,DATOS519,DATOS520,DATOS521,DATOS522,DATOS523,DATOS524,DATOS525,DATOS526,DATOS527,DATOS528,DATOS529,DATOS530,DATOS531,DATOS532,DATOS533,DATOS534,DATOS535,DATOS536,DATOS537,DATOS538,DATOS539,DATOS540,DATOS541,DATOS542,DATOS543,DATOS544,DATOS545,DATOS546,DATOS547,DATOS548,DATOS549,DATOS550,DATOS551,DATOS552,DATOS553,DATOS554,DATOS555,DATOS556,DATOS557,DATOS558,DATOS559,DATOS560,DATOS561,
DATOS562,DATOS563,DATOS564,DATOS565,DATOS566,DATOS567,DATOS568,DATOS569,DATOS570,DATOS571,DATOS572,DATOS573,DATOS574,DATOS575,DATOS576,DATOS577,DATOS578,DATOS579,DATOS580,DATOS581,DATOS582,DATOS583,DATOS584,DATOS585,DATOS586,DATOS587,DATOS588,DATOS589,DATOS590,DATOS591,DATOS592,DATOS593,DATOS594,DATOS595,DATOS596,DATOS597,DATOS598,DATOS599,DATOS600,
DATOS601,DATOS602,DATOS603,DATOS604,DATOS605,DATOS606,DATOS607,DATOS608,DATOS609,DATOS610,DATOS611,DATOS612,DATOS613,DATOS614,DATOS615,DATOS616,DATOS617,DATOS618,DATOS619,DATOS620,DATOS621,DATOS622,DATOS623,DATOS624,DATOS625,DATOS626,DATOS627,DATOS628,DATOS629,DATOS630,DATOS631,DATOS632,DATOS633,DATOS634,DATOS635,DATOS636,DATOS637,DATOS638,DATOS639,DATOS640,DATOS641,DATOS642,DATOS643,DATOS644,DATOS645,DATOS646,DATOS647,DATOS648'''
f = open ('indice_email.txt','r')
i = int(f.read())
f.close()

for elem in listadatos[i:107]:
    USUARIO=elem["USUARIO"]
    PASSWORD=elem["PASSWORD"]
    PASSWORD=elem["PASSWORD"]

    EMAILRECUPERACION=elem["EMAILRECUPERACION"]
    RESPUESTA="perro loco"
    print(f"Usuario: {USUARIO} PASS : {PASSWORD}")
    i+=1
    vpn = Windscribe("servers.txt","azuresilk03","Fps91507856")
    vpn.login("azuresilk07","Fps91507856")
    vpn.locations()
    vpn.connect("Vice")
    vpn.ipcheck()    
    
    iniciarbot(USUARIO,PASSWORD,EMAILRECUPERACION,RESPUESTA)
    
    f = open('indice_email.txt','w')
    f.write(str(i))
    f.close()
    print(i)
    time.sleep(5)


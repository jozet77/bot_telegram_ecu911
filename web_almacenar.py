#--------------------------------------------------
#
#Almacenamiento Release 0 build 1
#
#--------------------------------------------------
import json
import urllib.request
import psycopg2
import ssl

def tCamaras(lista=[], *lst):
	sumT = 0
	auxA = 0
	auxC = 0
	auxM = 0
	auxx = ""
	for canton in lista:
		auxx = jCamaras(canton)
		sumT = sumT + len(auxx['data'])
		for cam in auxx['data']:
			if(cam['estado'] == "Operativa"):
				auxA = auxA + 1
			elif(cam['estado'] == "No Operativa"):
				auxC = auxC + 1
			elif(cam['estado'] == "Con Solicitud de Mantenimiento"):
				auxM = auxM + 1
	return [sumT, auxA, auxC, auxM]
	
def jCamaras(numero):
	context = ssl._create_unverified_context()
	fo = open("C:\\Users\\Administrator\\Documents\\bot_telegram\\link.txt", "r+")
	link = fo.read(100);
	camUrl = link + str(numero)
	fo.close()
	aux =  json.loads(((urllib.request.urlopen(camUrl, context=context)).read()).decode("utf-8"))
	return aux

def imprimir(msg):
	return msg

def texto_camaras(texto):
	respuesta = [0,0,0,0]
	if (texto == "Quito"):
		lst = [207,208,209,210,211,212,213,214,198,199,200,201,202,249,248,250,251]
		respuesta = tCamaras(lst)
	
	if (texto == "Samborondon"):
		lst = [215,216,217,102,103,105,107,108,109,110,111,121,112,113,114,106,115,116,117,118,119,120,122,123,124,125,126,124]
		respuesta = tCamaras(lst)
	
	if (texto == "Babahoyo"):
		lst = [149,150,151,152,153,154,155,156,157,158,159,160,161]
		respuesta = tCamaras(lst)
	
	if (texto == "Austro"):
		lst = [27,28,29,30,31,32,33,34,35,26,36,37,38,39,40,48,49,50.51,52,53,54]
		respuesta = tCamaras(lst)
	
	if (texto == "Macas"):
		lst = [186,187,188,189,190,191,192,193,194,195,196,197]
		respuesta = tCamaras(lst)
	
	if (texto == "Machala"):
		lst = [78,79,80,81,82,83,84,85,86,87,88,89,90,91,236,237,238,239,240,241,242,243,244,245]
		respuesta = tCamaras(lst)
	
	if (texto == "Loja"):
		lst = [148,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147]
		respuesta = tCamaras(lst)
	
	if (texto == "Ambato"):
		lst = [226,227,228,229,230,231,232,233,234,235,71,72,73,74,75,76,77,203,204,205,206]
		respuesta = tCamaras(lst)
	
	if (texto == "Riobamba"):
		lst = [61,62,63,64,65,66,67,68,69,70]
		respuesta = tCamaras(lst)
	
	if (texto == "Portoviejo"):
		lst = [164,165,166,167,168,169,170,171,173,174,175,176,177178,179,180,181,182,183,184,185,162]
		respuesta = tCamaras(lst)
		
	if (texto == "Santo Domingo"):
		lst = [218,247]
		respuesta = tCamaras(lst)
		
	if (texto == "Ibarra"):
		lst = [127,128,129,130,131,132]
		respuesta = tCamaras(lst)
	
	if (texto == "Esmeraldas"):
		lst = [92,93,94,95,96,97,98,99,100]
		respuesta = tCamaras(lst)
	
	if (texto == "Tulcan"):
		lst = [55,56,57,58,59,60]
		respuesta = tCamaras(lst)
	
	if (texto == "Nueva Loja"):
		lst = [219,220,221,222,223,224,225]
		respuesta = tCamaras(lst)
	
	if (texto == "Galapagos"):
		lst = [101,252,253]
		respuesta = tCamaras(lst)
		
	return (respuesta)

def guardar(idd, resp=[], *res):
	cursor.execute("""UPDATE camaras SET operativas = %(ocupados)s, caidas = %(caidas)s, mantenimiento = %(mante)s, total = %(total)s
		WHERE id = %(id)s;""",{'ocupados': resp[2], 'caidas': resp[1],'mante': resp[3],'total': resp[0], 'id':idd})

try:
	connect_str = "dbname='TELEGRAM' user='postgres' host='localhost' " + \
		"password='3st@d1st1c@s2016'"
	conn = psycopg2.connect(connect_str)
	cursor = conn.cursor()
	guardar(1,(texto_camaras("Samborondon")))
	guardar(2,(texto_camaras("Quito")))
	guardar(12,(texto_camaras("Babahoyo")))
	guardar(3,(texto_camaras("Austro")))
	guardar(4,(texto_camaras("Ambato")))
	guardar(14,(texto_camaras("Macas")))
	guardar(7,(texto_camaras("Machala")))
	guardar(16,(texto_camaras("Loja")))
	guardar(15,(texto_camaras("Riobamba")))
	guardar(5,(texto_camaras("Portoviejo")))
	guardar(11,(texto_camaras("Santo Domingo")))
	guardar(6,(texto_camaras("Ibarra")))
	guardar(8,(texto_camaras("Esmeraldas")))
	guardar(9,(texto_camaras("Tulcan")))
	guardar(10,(texto_camaras("Nueva Loja")))
	guardar(13,(texto_camaras("Galapagos")))
	conn.commit()
	cursor.close()
except Exception as e:
	print("Uh oh, can't connect. Invalid dbname, user or password?")
	print(e)

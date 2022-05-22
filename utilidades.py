import re
import datetime
import os
import json


nombre = ''
apellido = ''
tipodoc = ''
id = int()
correo = ''
rh = ''
numero = int()

datos = {'Nombre': nombre, 'Apellido': apellido, 'Tipo de documento': tipodoc, 'Cedula': id, 'Correo': correo, 'RH': rh, 'Celular': numero}


class db:
	def __init__(self, nombre, apellido, tipodoc, id, correo, rh, numero):
		self.Nombre = nombre
		self.Apellido = apellido
		self.Tipodoc = tipodoc
		self.Cedula = id
		self.Correo = correo
		self.RH = rh
		self.Ceular = numero
	def registrar_usuario(datos):
		datos = {'Nombre': nombre, 'Apellido': apellido, 'Tipo de documento': tipodoc, 'Cedula': id, 'Correo': correo, 'RH': rh, 'Celular': numero}
		global f
		with open("/home/runner/Reto-5-ksenas95/database.txt", 'w') as f:
			json.dump(datos, f)
			f.write(os.linesep)
			f.close()
			return f
	def vtipo_doc(s ):
		if(tipodoc == 'CC' or tipodoc == 'TI' or tipodoc == 'PA' or tipodoc == 'CE'):
			return True
		else:
			return False

	def vnumero_doc(numero_doc):
		if(numero_doc.isnumeric() and len(numero_doc) <= 12):
			return True
		else:
			return False

	def vnombre(nombre):
		if(nombre.isalpha() and len(nombre)<=30):
			return True
		else:
			return False

	def vapellido(apellido):
		if(apellido.isalpha() and len(apellido)<=30):
			return True
		else:
			return False

	def vfecha(fecha):
		if(len(fecha)<=10):
			return True
		else:
			return False

	def vrh_gs(rh):
		if (len(rh)==2):
			if  (rh[0]=="O" or rh[0]=="A" or rh[0]=="B")and(rh[1] == "+" or rh[1] == "-"):
				return True
			else:
				return False
		else:
			return False

	def vcorreo(correo):
		if(len(correo)<=50 and re.match('^[(a-z0-9\_\-\.)]{3,10}@[(a-z0-9\_\-)]{3,}\.[(a-z)]{2,3}$',correo.lower())):
			return True
		else:
			return False
    
	def vnumero_tel(numero):
		if(len(numero) <11 and numero.isnumeric()):
			return True
		else:
			return False

	def validar_usuario(tipodoc,id,nombre,apellido,fecha,rh,correo,numero):
		if (tipodoc() and
      	id() and
      	nombre() and
      	apellido() and
      	fecha() and
      	rh() and
      	correo() and
      	numero()) == f:
					return True
		else:
			return False
	def Validar_Existente(datos, id):
		for datos in datos:
			if datos['Numero de documento'] == id:
				print("Ya esta registrado")
				return True
			else:
				print("No esta registrado")
				return False 



	def validar_fecha_cita(fecha_cita):
	    if datetime.strptime(fecha_cita, '%Y-%m-%d') > datetime.now():
	        return True
	    else:
	        return False
	
	def agendar_citas(datos, id, fecha):
		existe = Validar_Existente(datos, id)
		if existe :
			fecha_date = datetime.strptime(fecha, '%Y-%m-%d').date()
			if validar_fecha_cita(fecha_date):
				return fecha_date
			else:
				return False

	def visualizar_usuarios(tipodoc, id, nombre, apellido, fecha, rh, correo, numero):
	
	  vista = print(f"""\n  -*-*-*-*-*-*-*-*-*-*-*-  
	  | Tipo de Doc.\t | {tipodoc} | 
	  -*-*-*-*-*-*-*-*-*-*-*-  
	  | Numero de Doc.\t | {id} | 
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | Nombre.\t | {nombre} | 
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | Apellido.\t | {apellido} | 
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | Fecha de Nacimiento.\t | {fecha} | 
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | Tipo de sangre.\t | {rh[0]} {rh[1]} | 
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | Correo.\t | {correo} |
	  -*-*-*-*-*-*-*-*-*-*-*-
	  | número.\t | {numero} |                  
	  -*-*-*-*-*-*-*-*-*-*-*-\n""")
	  return vista

	
	
		
	
		
	
	
	



	
from datetime import datetime
import os
import time
import utilidades as ut

def menu_principal():
  print("""Menu principal
      1 - Registrar Usuario.
      2 - Visulizar Usuarios registrados.
      3 - Agendar Citas.
      4 - Salir.""")
      
option = int()

menu_principal()
time.sleep(4)

while True:
  os.system('clear')
  print('Ingrese la opcion \n')
  option = int(input())
  try:
    if option == 1:
      tipo_doc = input('Cual es tu tipo de documento?\t (CC,PA,TI o CE)\n  => ').upper()
      os.system ("clear")
import os
import time
import utilidades as ut

#Main Menu
Programa = """+---------------------------------------------------+
| +-----------------------------------------------+ |
| | +-------------------------------------------+ | |
| | | Inicializando programa para agendar citas | | |
| | +-------------------------------------------+ | |
| +-----------------------------------------------+ |
+---------------------------------------------------+
"""
print(Programa)

time.sleep(3)

menu = [
    '1 - Registrar Usuario\n', '2 - Visualizar Usuarios Registrados\n',
    '3 - Agendar Citas\n', '4 - Salir\n'
]

for i in range(0, 4):
    print(menu[i])

opcion = int(input("Por favor ingrese la opcion: "))


def main_menu(opcion):
    op = int(input)
    while op != 4:
        try:
            if op == 1:
                os.system('clear')
                print(
                    """Registrando Usuario, por favor, ingrese los siguientes datos:
						Nombre:
						Apellido:
						Tipo de documento:
						Numero de documento:
						Fecha de naciemiento:
						Grupo Sanguíneo:
						Correo:
						Numero de telefono:
						""")
        except:
            if op != 4:
                print(
                    "Ha seleccionado una opcion errónea, por favor intentelo de nuevo:"
                )
                print(menu)
                time.sleep(4)
                main_menu()

    main_menu(opcion)

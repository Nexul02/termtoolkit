import os
import time


class Clasificador:

    def __init__(self):
        global menu

        menu = """        
        Menú de opciones

        1. Listar directorio
        2. Crear carpeta
        3. Eliminar carpeta
        4. Mostrar menú
        5. Salir
        """
        print("****  CLASIFICADOR DE ARCHIVOS ****\n")
        print(menu)

        while True:
            op = input("Introduzca una opción: ")
            output = self.choption(op)
            if output == "break":
                print("Saliendo de la aplicacion...")
                time.sleep(3)
                break
            else:
                print(output)

    def choption(self, op):
        if op == "1":
            return self.directory_list()
        elif op == "2":
            return self.mkdir()
        elif op == "3":
            return self.rmdir()
        elif op == "4":
            return menu
        elif op == "5":
            return "break"
        else:
            return "\nOpcion invalida\n"

    def directory_list(self):
        path = input("\nIntroduzca una ruta: ")
        try:
            current_folder = os.listdir(path)
            return current_folder
        except:
            return "Ruta invalida."

    def mkdir(self):
        path = input("\nIngresa nombre de la carpeta a crear: ")
        os.mkdir(path)
        return f"\nEl directorio {path}/ se ha creado con exito...\n"

    def rmdir(self):
        path = input("\nIngrese la ruta de la carpeta a eliminar: ")
        try:
            os.rmdir(path)
            return f"\nEl directorio {path} se ha eliminado con exito...\n"
        except:
            return "\nError\n"


if __name__ == '__main__':
    directory = Clasificador()

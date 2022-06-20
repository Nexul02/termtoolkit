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
        4. Ver ruta actual
        5. Cambiar directorio
        6. Mostrar menú
        7. Salir
        """
        print("****  CLASIFICADOR DE ARCHIVOS ****\n")
        print(menu)

        while True:
            print("\nIntroduzca una opcion")
            op = input("$ ")
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
            return f"\nRuta actual: {self.current_directory()}"
        elif op == "5":
            return self.chdir()
        elif op == "6":
            return menu
        elif op == "7":
            return "break"
        else:
            return "\nOpcion invalida\n"

    def current_directory(self):
        current_dir = os.getcwd()
        return current_dir

    def directory_list(self):
        path = self.current_directory()
        current_folder = os.listdir(path)
        return current_folder

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

    def chdir(self):
        print("\nIntroduzca la ruta")
        path = input("$ ")
        os.chdir(path)
        return f"\n Cambiando a {path}..."


if __name__ == '__main__':
    directory = Clasificador()

import sqlite3
import time

#db = sqlite3.connect(':memory:') # Base de datos en memoria

# La base de datos "prueba.db" fue creada directamente desde DB Browser for SQLite
""" Este programa hace uso de esa base de datos para consultar la tabla libro; donde se pueden realizar 3 funciones:
    basicas, buscar un libro, agregar o elimanr un libro de la tabla, usando la llave ISBN. 
"""
# Existen dos Filas (libros) en la Tabla Libros. El primero libro tiene el ISBN = 1234. El segundo tiene el ISBN = 12345.

# Se debe usar la ruta absoluta del archivo de base de dato que contiene la tabla, para poder conectarse
db = sqlite3.connect("C:\\Users\\Ryan Tygart\\Dropbox\\PycharmProjects\\Clase2\\prueba.db") # Base de datos en un archivo

while True:
    print(" \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t LIBROS")
    print(" \n\n\tSeleccione uno de las siguientes acciones:")
    Opcion = int(input("\t\t 1. Buscar un libro \n\t\t 2. Agregar un libro \n\t\t 3. Eliminar un libro \n\t\t\t Su elección: "))

    cursor = db.cursor()

# La Opcion 1 permite buscar un libro usando un ISBN especifico
    if Opcion == 1:
        ISBN = input("\n\n\tPara buscar un libro, favor ingresar su ISBN: ")
        cursor.execute('''SELECT Nombre, Autor FROM Libro WHERE ISBN = ?''', (ISBN,))
        resultado = cursor.fetchall()
        print("\t\t", resultado, "\n")
        db.commit()
        break

# La Opcion 2 agrega una fila con todas las columnas correspondientes
    elif Opcion == 2:
        print("\n\t Introduzca los siguientes datos solicitados: ")
        ISBN = input("\t\tISBN: ")
        Nombre = input("\t\tNombre del libro: ")
        Autor = input("\t\tNombre del autor: ")
        Publicacion = input("\t\tAño de publicacion: ")
        Cantidad_Paginas = input("\t\tCantidad de paginas:")

        cursor.execute('''INSERT INTO Libro(ISBN, Nombre, Autor, Publicacion, Cantidad_Paginas)
                  VALUES(?,?,?,?,?)''', (ISBN, Nombre, Autor, Publicacion, Cantidad_Paginas))
        db.commit()
        break

# La Opcion 3 elimina un libro existente utilizando el ISBN como llave.
    elif Opcion == 3:
        ISBN = input("Introduzca el ISBN del libro que quiere eliminar: ")
        cursor.execute('''DELETE FROM Libro WHERE ISBN = ?''',(ISBN,)) # Se le pone coma desps de ISBN por que no puede elimaniar sola esa columna debe eliminar todo lo que esta en esa fila. La coma permite incluir todas las columnas restantes sin tener que nombrarlas.
        db.commit()
        break

    print("OPCIÓN EQUIVOCADA. INTENTE NUVEAMENTE")
    time.sleep(1)

db.close()

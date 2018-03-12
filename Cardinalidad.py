import sqlite3
import time

#db = sqlite3.connect(':memory:') # Base de datos en memoria

# La base de datos "prueba.db" fue creada directamente desde DB Browser for SQLite
""" Este programa hace uso de esa base de datos para consultar la tabla libro; donde se pueden realizar 3 funciones:
    basicas, buscar un libro, agregar o elimanr un libro de la tabla, usando la llave ISBN. 
"""
"""Existen 5 flas con informacion de personas """

# Se debe usar la ruta absoluta del archivo de base de dato que contiene la tabla, para poder conectarse
db = sqlite3.connect("C:\\Users\\Ryan Tygart\\Dropbox\\PycharmProjects\\Tarea3\\Cardinalidad.db") # Base de datos en un archivo

while True:
    print(" \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t RELACIONES")
    print(" \n\n\tSeleccione una de las siguientes opciones:")
    Opcion = int(input("\t\t 1. Ver Personas \n\t\t 2. Agregar una Persona \n\t\t 3. Establecer Parentesco \n\t\t 4. Ver Familias \n\t\t 5. Eliminar una Persona \n\t\t\t Su elección: "))

    cursor = db.cursor()

# La Opcion 1 permite ver la lista de personas que existen en la tabla.
    if Opcion == 1:
        print("\n\n\t Las personas existentes en la base de datos son: ")
        cursor.execute('''SELECT * FROM Personas''')
        resultado = (cursor.fetchall())
        for a in resultado:
            print("Identificacion: ", a[0])
            print("Nombre: ", a[1])
            print("Apellido: ", a[2])
            print("Lugar de Nacimiento: ", a[3])
            print("Año de Nacimiento: ", a[4], "\n")


#        for resultado in resultado:
#            print("\t\t", resultado, "\n")
        db.commit()
        break

# La Opcion 2 agrega una fila con todas las columnas correspondientes
    elif Opcion == 2:
        print("\n\t Introduzca los siguientes datos solicitados: ")
        Identificacion = input("\t\t Numero de Indentidad: ")
        Nombre = input("\t\t Nombre: ")
        Apellido = input("\t\t Apellido: ")
        Lugar_Nacimiento = input("\t\t Lugar de nacimiento: ")
        Año_Nacimiento = input("\t\t Año de nacimiento:")

        cursor.execute('''INSERT INTO Personas(Identificacion, Nombre, Apellido, Lugar_Nacimiento, Año_Nacimiento)
                  VALUES(?,?,?,?,?)''', (Identificacion, Nombre, Apellido, Lugar_Nacimiento, Año_Nacimiento))
        db.commit()
        break

# La Opcion 3 es para establecer una relacion entre las tablas Personas y Familia .
    elif Opcion == 3:
        print("\n\n\t Las personas existentes en la base de datos son: ")
        cursor.execute('''SELECT * FROM Personas''')
        resultado = (cursor.fetchall())
        for a in resultado:
            print("Nombre: ", a[1])

        print("\n\n\t Las posibles relaciones en la base de datos son: ")
        cursor.execute('''SELECT * FROM Familia''')
        resultado = (cursor.fetchall())
        for a in resultado:
            print("Parentesco: ", a[1])

        print("\n\t Introduzca los siguientes datos solicitados: ")
        Persona = input("\t\t Nombre de la primera persona: ")
        Parentesco = input("\t\t Parentesco a establecer establecer: ")
        Persona2 = input("\t\t Nombre de la segunda persona: ")

        cursor.execute('''INSERT INTO Parentesco(Persona, Parentesco, Persona2)
                          VALUES(?,?,?)''', (Persona, Parentesco, Persona2))
        print("\n\t\tSu adiccion a sido guardado exitosamente")
        print("\t\t", Persona, "es", Parentesco, "de", Persona2)
        db.commit()
        break

# La Opcion 4 es para contemplar la informacion en la tabla de Parentesco que se formo como resultado del la relacion muchos a muchos entre la tabla Familia y Personas.
    elif Opcion == 4:
        print("\n\n\t Estas son las relaciones establecidas en la base de datos: ")
        cursor.execute('''SELECT * FROM Parentesco''')
        resultado = (cursor.fetchall())
        for a in resultado:
            print(a[0], "es", a[1], "de", a[2] )
        #print("Nombre: ", a[1], "\n")
        #print("Apellido: ", a[2])
        db.commit()
        break


# La Opcion 5 es para eliminar una fila que continene la informacion de una persona .
    elif Opcion == 5:
        Identificacion = input("Introduzca el nuemro de indentificacion personal de la persona que desea eliminar: ")
        cursor.execute('''DELETE FROM Personas WHERE Identificacion = ?''',(Indentificacion,)) # Se le pone coma desps de ISBN por que no puede elimaniar sola esa columna debe eliminar todo lo que esta en esa fila. La coma permite incluir todas las columnas restantes sin tener que nombrarlas.
        db.commit()
        break

    print("OPCIÓN EQUIVOCADA. INTENTE NUVEAMENTE")
    time.sleep(1)

db.close()

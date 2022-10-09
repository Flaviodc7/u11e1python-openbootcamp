import sqlite3


def delete_create_db():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    querya = f"DROP TABLE alumnos;"

    cursor.execute(querya)

    queryb = f"CREATE TABLE alumnos(" \
             f"id INTEGER PRIMARY KEY," \
             f"nombre TEXT NOT NULL," \
             f"apellido TEXT NOT NULL);"

    cursor.execute(queryb)
    conn.commit()
    cursor.close()
    conn.close()


def insert_data():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    alumnos = [
        ["Jorge", "Calamar"],
        ["Eduardo", "Bonaparte"],
        ["Miguel", "Acevedo"],
        ["Alfonso", "Guimaraez"],
        ["Daniel", "Eustaquio"],
        ["Manuel", "Kollias"],
        ["Coniglio", "Buenaventura"],
        ["Martín", "Rios"]
    ]
    id = 1

    for alumno in alumnos:
        query = f"INSERT INTO alumnos (id, nombre, apellido) VALUES({id}, '{alumno[0]}', '{alumno[1]}')"
        cursor.execute(query)
        conn.commit()
        id += 1

    cursor.close()
    conn.close()


def search_student(name):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE nombre='{name}'"
    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()
    if data is not None:
        return f"El alumno encontrado es: {data[1]} {data[2]}"
    else:
        return "Alumno no encontrado"


def main():
    delete_create_db()
    insert_data()
    alumno = input("Ingrese nombre de alumno a buscar: ")

    print(search_student(alumno))


if __name__ == '__main__':
    main()

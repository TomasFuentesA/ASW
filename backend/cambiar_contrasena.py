import psycopg2
import time


def connection():
    conn = psycopg2.connect(host="db", database="sistema_medico", user="postgres", password="postgres")
    return conn

def service_cambio_contrasena(mail, password):
    time.sleep(5)
    conn = connection()
    cursor = conn.cursor()
    try: 
        statement = "UPDATE SET cuenta.contrasena = '"+password+"' FROM cuenta WHERE correo ='"+mail+"';"
        cursor.execute(statement)
        statement.fetchone()
        return True
    except:
        return False
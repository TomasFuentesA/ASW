import psycopg2
import time

def connection():
    conn = psycopg2.connect(host="db", database="sistema_medico", user="postgres", password="postgres")
    return conn

def service_login(mail, password):
    time.sleep(5)
    conn = connection()
    cursor = conn.cursor()
    try: 
        statement = "SELECT * FROM cuenta WHERE correo = '" + mail + "' AND contrasena = '"+password+"';"
        cursor.execute(statement, [mail, password])
        return (True, cursor.fetchone())

    except:
        return False
import psycopg2

def connection():
    conn = psycopg2.connect(host="localhost", database="sistema_medico", user="postgres", password="postgres")
    return conn

def service_login(mail, password):
    conn = connection()
    cursor = conn.cursor()
    try: 
        statement = "SELECT * FROM cuentas WHERE correo = ? AND contrasena = ?"
        cursor.execute(statement, [mail, password])
        return True

    except:
        return False
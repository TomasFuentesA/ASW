import psycopg2

def connection():
    conn = psycopg2.connect(host="localhost", database="sistema_medico", user="postgres", password="postgres")
    return conn

def service_cambio_contrasena(mail, password):
    conn = connection()
    cursor = conn.cursor()
    try: 
        statement = "UPDATE SET cuentas.contrasena = '"+password+"' FROM cuentas WHERE correo ='"+mail+"';"
        cursor.execute(statement)
        statement.fetchone()
        return True
    except:
        return False
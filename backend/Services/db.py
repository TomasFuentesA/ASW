import psycopg2
import time

def connection():
    conn = psycopg2.connect(host="db", database="sistema_medico", user="postgres", password="postgres")
    return conn
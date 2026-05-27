from mysql.connector.pooling import MySQLConnectionPool

pool = MySQLConnectionPool(
    pool_name="escuela_pool",
    pool_size=5,
    host="localhost",
    user="root",
    password="",
    database="sistemas_escuela"
)

def obtener_conexion():
    return pool.get_connection()
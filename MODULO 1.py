def create_conn():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="PROYECTOICFES",
        user="conector",
        password="Proyectofinal"
    )
    return conn

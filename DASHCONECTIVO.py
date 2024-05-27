import dash
from dash import dcc, html
import plotly.express as px
import psycopg2
import pandas as pd

def create_conn():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="PROYECTOICFES",
        user="conector",
        password="Proyectofinal"
    )
    return conn

def fetch_data(conn, query):
    df = pd.read_sql_query(query, conn)
    return df

app = dash.Dash(__name__)

# Consultas para obtener datos de cada tabla
df_estudiante = fetch_data(create_conn(), "SELECT * FROM Estudiante")
df_familia = fetch_data(create_conn(), "SELECT * FROM Familia")
df_colegio = fetch_data(create_conn(), "SELECT * FROM Colegio")
df_examen_icfes = fetch_data(create_conn(), "SELECT * FROM Examen_ICFES")
df_estudiante_colegio = fetch_data(create_conn(), "SELECT * FROM Estudiante_Colegio")

# Crear figuras para cada tabla
fig_estudiante = px.bar(df_estudiante, x='género', y='horas_sem_trabajadas', color='municipio_residencia')
fig_familia = px.bar(df_familia, x='estrato', y='num_personas_hogar')
fig_colegio = px.bar(df_colegio, x='género_colegio', y='colegio_consecutivo')
fig_examen_icfes = px.bar(df_examen_icfes, x='puntaje_global', y='puntaje_lecturacritica')
fig_estudiante_colegio = px.bar(df_estudiante_colegio, x='estu_consecutivo', y='colegio_consecutivo')

app.layout = html.Div(children=[
    html.H1(children='Análisis de datos'),

    html.Div(children='Visualización de los datos de la tabla Estudiante.'),
    dcc.Graph(id='estudiante-graph', figure=fig_estudiante),

    html.Div(children='Visualización de los datos de la tabla Familia.'),
    dcc.Graph(id='familia-graph', figure=fig_familia),

    html.Div(children='Visualización de los datos de la tabla Colegio.'),
    dcc.Graph(id='colegio-graph', figure=fig_colegio),

    html.Div(children='Visualización de los datos de la tabla Examen_ICFES.'),
    dcc.Graph(id='examen_icfes-graph', figure=fig_examen_icfes),

    html.Div(children='Visualización de los datos de la tabla Estudiante_Colegio.'),
    dcc.Graph(id='estudiante_colegio-graph', figure=fig_estudiante_colegio),
])

if __name__ == '__main__':
    app.run_server(debug=True)

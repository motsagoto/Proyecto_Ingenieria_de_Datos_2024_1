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

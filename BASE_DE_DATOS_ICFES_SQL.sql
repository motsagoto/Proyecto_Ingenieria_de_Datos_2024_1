

CREATE TABLE Estudiante (
    Estu_consecutivo VARCHAR(20) PRIMARY KEY,
    Tipo_documento VARCHAR(20),
    Género VARCHAR(20),
    Municipio_residencia VARCHAR(50),
    Lectura_diaria VARCHAR(5),
    Dedicación_internet VARCHAR(20),
    Horas_sem_trabajadas INT
);

CREATE TABLE Familia (
    Familia_consecutivo SERIAL PRIMARY KEY,
    Estu_consecutivo VARCHAR(20) UNIQUE,
    Estrato INT,
    Num_personas_hogar INT,
    Nivel_edu_padres VARCHAR(50),
    Situacion_lab_padres VARCHAR(50),
    Acceso_internet BOOLEAN,
    Acceso_computadora BOOLEAN,
    Acceso_consola BOOLEAN,
    Fami_comecamespescadohuevo BOOLEAN,
    FOREIGN KEY (Estu_consecutivo) REFERENCES Estudiante(Estu_consecutivo)
);

CREATE TABLE Colegio (
    Colegio_consecutivo SERIAL PRIMARY KEY,
    Nombre_establecimiento VARCHAR(100),
    Género_colegio VARCHAR(20),
    Bilingue BOOLEAN,
    Area_ubicación VARCHAR(50),
    Jornada_escolar VARCHAR(20)
);

CREATE TABLE Examen_ICFES (
    Examen_consecutivo SERIAL PRIMARY KEY,
    Estu_consecutivo VARCHAR(20) UNIQUE,
    Puntaje_lecturacritica INT,
    Puntaje_matematicas INT,
    Puntaje_ciencia_naturales INT,
    Puntaje_ciencia_sociales INT,
    Puntaje_inglés INT,
    Puntaje_global INT,
    Percentil INT,
    Desempeño VARCHAR(255),
    FOREIGN KEY (Estu_consecutivo) REFERENCES Estudiante(Estu_consecutivo)
);

-- Tabla Estudiante_Colegio para manejar la relación entre estudiantes y colegios
CREATE TABLE Estudiante_Colegio (
    Estu_consecutivo VARCHAR(20),
    Colegio_consecutivo SERIAL,
    FOREIGN KEY (Estu_consecutivo) REFERENCES Estudiante(Estu_consecutivo),
    FOREIGN KEY (Colegio_consecutivo) REFERENCES Colegio(Colegio_consecutivo)
);


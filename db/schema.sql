DROP TABLE IF EXISTS cuenta;
DROP TABLE IF EXISTS paciente;
DROP TABLE IF EXISTS diagnostico_medico;

CREATE TABLE cuenta(
   id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,
   correo TEXT UNIQUE NOT NULL,
   contrasena TEXT NOT NULL,
   nombre_s TEXT NOT NULL,
   apellido_s TEXT NOT NULL,
   especialidad TEXT,
   flag_contrasena boolean NOT NULL
);

CREATE TABLE paciente (
   id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
   nombre_s TEXT NOT NULL,
   apellido_s TEXT NOT NULL,
   edad INTEGER NOT NULL,
   sexo INTEGER NOT NULL,
   contacto INTEGER,
   contacto_emergencia  INTEGER,
   direccion TEXT,
   tipo_sangre  INTEGER,
   anotaciones TEXT
);

CREATE TABLE diagnostico_medico (
   id_diagnostico INTEGER PRIMARY KEY,
   id_cuenta INTEGER NOT NULL,
   id_paciente TEXT NOT NULL,
   diagnostico TEXT NOT NULL,
   informacion_adicional TEXT,
   tratamiento TEXT,
   fecha_diagnostico TEXT NOT NULL,
   FOREIGN KEY(id_paciente) REFERENCES paciente (id_paciente),
   FOREIGN KEY(id_cuenta) REFERENCES cuenta (id_cuenta)
);


INSERT INTEGERO cuenta(id_cuenta, correo, contrasena, nombre_s,apellido_s,especialidad,flag_contrasena)
VALUES(0,'admin@admin.cl','admin1234','admin','admin','admin',TRUE),
      (1,'medico1@medico1.cl','medico1234','medico1','medico1','Neurocirujano',FALSE);
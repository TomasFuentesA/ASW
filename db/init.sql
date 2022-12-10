CREATE TABLE [IF NOT EXISTS] cuenta (
   id_cuenta SERIAL PRIMARY KEY,
   correo varchar(255) NOT NULL,
   contrasena varchar(255) NOT NULL,
   nombre_s varchar(255) NOT NULL,
   apellido_s varchar(255) NOT NULL,
   especialidad varchar(255),
);
CREATE TABLE [IF NOT EXISTS] diagnostico_medico (
   id_diagnostico SERIAL PRIMARY KEY,
   id_cuenta SERIAL NOT NULL,
   id_paciente varchar(9) NOT NULL,
   diagnostico varchar(1000) NOT NULL,
   informacion_adicional varchar(500),
   tratamiento char(1000),
   fecha_diagnostico date NOT NULL,
   CONSTRAINT FOREIGN KEY(id_paciente) REFERENCES paciente (id_paciente),
   CONSTRAINT FOREIGN KEY(id_cuenta) REFERENCES cuenta (id_cuenta)
);

CREATE TABLE [IF NOT EXISTS] paciente (
   id_paciente varchar(9) NOT NULL PRIMARY KEY,
   nombre_s varchar(255) NOT NULL,
   apellido_s varchar(255) NOT NULL,
   edad int(3) NOT NULL,
   sexo int(1) NOT NULL,
   contacto int(12),
   contacto_emergencia  int(12),
   direccion varchar(255),
   tipo_sangre  int(1),
   anotaciones varchar(255),
);

INSERT INTO cuenta(id_cuenta, correo, contrasena, nombre_s,apellido_s)
VALUES(0,'admin@admin.cl','admin1234','admin','admin'),
      (1,'medico1@medico1.cl','medico1234','medico1','medico1');
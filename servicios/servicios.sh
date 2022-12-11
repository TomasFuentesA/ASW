#!/bin/sh
python3 auth.py & python3 Sagregar_cuenta.py \
& python3 Sagregar_diagnostico.py & python3 Sagregar_paciente.py \
& python3 Scambio_pw.py & python3 Sdelete_medico.py \
& python3 Sdelete_paciente.py & python3 Shistorial_medico.py \
& python3 Sedit_paciente.py
#!/bin/bash

# Nombre del entorno virtual
VENV_DIR="venv"

# Crear el entorno virtual si no existe
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
    echo "Entorno virtual creado en $VENV_DIR"
fi

# Activar el entorno virtual
source $VENV_DIR/bin/activate

# Instalar los paquetes desde requirements.txt
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Paquetes instalados desde requirements.txt"
else
    echo "Archivo requirements.txt no encontrado"
fi

# Mantener el entorno virtual activado
$SHELL
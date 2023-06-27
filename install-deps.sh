#!/bin/bash

# Verificar si NVM está instalado
if command -v nvm &>/dev/null; then
  echo "NVM está instalado"
  # Activar NVM
  source ~/.nvm/nvm.sh
  # Ejecutar 'npm install'
  npm install
else
  echo "NVM no está instalado"
  # Instalar NVM
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
  # Activar NVM
  source ~/.nvm/nvm.sh
  # Instalar Node.js v14.21.3
  nvm install 14.21.3
  # Ejecutar 'npm install'
  npm install
fi
#!/bin/bash

docker compose up -d --build

# Vérifie le système d'exploitation
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  open -a Safari http://localhost:8000
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows (utilisation de commandes spécifiques à Windows)
  start chrome http://localhost:8000
else
  # Système d'exploitation par défaut pour le navigateur local
  echo "Le navigateur local n'est pas supporté sur ce système."
fi
#!/bin/bash

# Exemple de bash entrypoint pout postgres


# configure les flags d'erreur
set -o errexit
set -o pipefail
set -o nounset

# lancement des commandes au demarrage du container
# 0.0.0.0 pour ecouter sur toutes les interfaces
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
# script_doctest.py
import doctest
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CitasMedicas.settings')
django.setup()

import CitasMed.views  # Asegúrate de que el import sea correcto

if __name__ == "__main__":
    doctest.testmod(CitasMed.views)

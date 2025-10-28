import pytest

#Archivos de prueba a ejecutar

test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py"
]

#Argumentos para ejecutar las pruebas: los archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","-v"]

pytest.main(pytest_args)
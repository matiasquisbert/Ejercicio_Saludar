# Proyecto Saludo (Django + arquitectura hexagonal)

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

Probar en Postman: POST http://127.0.0.1:8000/api/saludar/
Body (raw JSON): {"nombre": "Gabo"}

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from saludo.application.services.saludar_service import SaludarService
from saludo.domain.persona import Persona


@csrf_exempt
def saludar(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    try:
        data = json.loads(request.body)
        nombre = data["nombre"]
    except (json.JSONDecodeError, KeyError):
        return JsonResponse({"error": "Se requiere el campo 'nombre'"}, status=400)
    mensaje = SaludarService().saludar(Persona(nombre))
    return JsonResponse({"mensaje": mensaje})

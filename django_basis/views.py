from django.http import JsonResponse

def myBaseService(request):
    data = {
        'clave': 'valor',
        'mensaje': '¡Hola, este es mi servicio en Django!'
    }
    return JsonResponse(data)

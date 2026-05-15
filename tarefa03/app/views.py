from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def usuarios(request):
    lista_usuarios = [
        {"nome": "Pedro", "matrícula": 1234, "idade": 17, "cidade": "natal"},
        {"nome": "Lucca", "matrícula": 4321, "idade": 7, "cidade": "natal"},
        {"nome": "Lady", "matrícula": 5678, "idade": 1, "cidade": "natal"},
        {"nome": "Loki", "matrícula": 8765, "idade": 4, "cidade": "natal"},
        {"nome": "Laila", "matrícula": 9101, "idade": 3, "cidade": "natal"},
    ]

    context = {
        "usuarios" : lista_usuarios
    }
    return render(request, "usuarios.html", context)
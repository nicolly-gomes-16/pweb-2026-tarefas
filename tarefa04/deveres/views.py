from django.shortcuts import render
from .models import Dever
from datetime import date

def deveres(request):
    deveres = Dever.objects.all()
    hoje = date.today()

    for dever in deveres:
        dever.atrasada = dever.prazo < hoje

    context = {
        "deveres": deveres,
        "hoje": hoje,
    }

    return render(request, "deveres/dever.html", context)
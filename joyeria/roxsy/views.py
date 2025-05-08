from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    productos= Producto.objects.all()
    context= {'productos': productos}
    return render(request, "joyeria/index.html", context)

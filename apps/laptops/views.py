"""
    vistas
"""
from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopForm
# funciones de vistas.
def principal(request):
    """
    funcion de la vista principal
    """
    laptops_listadas = Laptop.objects.all()
    return render(request,'contenido.html', {"compu":laptops_listadas})

#crud
def registrar(request):
    """
    funcion que registra compus
    """
    if request.method== 'POST':
        procesador = request.POST['kprocesador']
        generacion = request.POST['kgeneracion']
        sistema = request.POST['ksistema']
        ram = request.POST['kram']
        rom = request.POST['krom']
        comp=Laptop.objects.create(procesador=procesador,generacion=generacion,sistema=sistema,ram=ram,rom=rom)
        return redirect('/')

def eliminar(request, id):
    """
    funcion que elimina con id
    """
    if request.method=='GET':
        copp=Laptop.objects.get(id=id)
        copp.delete()
        return redirect('/')

def vistaeditar(request,id):
    """
    funcion que envia a la vista de editar
    """
    laptop = Laptop.objects.get(id=id)  # Obtener la instancia existente

    return render(request,'editfrm.html', {"laptop":laptop})

def funcioneditar(request, id):
    """
    Función que edita los objetos Laptop.
    """
    if request.method=='POST':
        procesador = request.POST['kprocesador']
        generacion = request.POST['kgeneracion']
        sistema = request.POST['ksistema']
        ram = request.POST['kram']
        rom = request.POST['krom']
        laptop = Laptop.objects.get(id=id)
        laptop.procesador=procesador
        laptop.generacion=generacion
        laptop.sistema=sistema
        laptop.ram=ram
        laptop.rom=rom
        laptop.save()
        return redirect('/')
    
def vistaprb(request):
    """
    Función que manda a la vista prb .
    """
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LaptopForm()
    return render(request,'prb.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Userbc21
from .forms import Userbc21Form1, Userbc21Form2



def registrate(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        return redirect('registrate-2', nombre, email, telefono)
    return render(request, 'biocarb21\\registrate.html')

def registrate_2(request, nombre, email, telefono):
    if request.method == "POST":
        form = Userbc21Form2(request.POST)
        if form.is_valid():
            form.save().nombre = nombre
            form.save().email = email
            form.save().telefono = telefono
            form.save()
            return redirect('registrate-exito')
    else:
        form = Userbc21Form2()
    context = {'form' : form}
    return render(request, 'biocarb21\\registrate-2.html', context)

def registrate_exito(request, user_id):
    user = Userbc21.objects.get(id = user_id)
    return render(request, 'biocarb21\\registrate-exito.html')#, context





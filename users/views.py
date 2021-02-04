from django.shortcuts import render,redirect
# importo el form que modifique
from .forms import RegisterForm
# importo el modelo user y el credit card para conectarlos en home
from django.contrib.auth.models import User
from credit_card.models import CreditCard
# importo el decorador, recordar cambiar la redireccion que hace en settings
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    # si se lleno el formulario y se envio en metodo post hago una cosa, sino meustro el form para que lo complete
    if(request.method == 'POST'):
        # tomo los valores del form
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            # agarro el username
            username = form.cleaned_data.get('username')
            # creo el mensaje de exito, tengo que importarlo arriba
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def index(request):
    context = None

    # voy a chequear si una tarjeta de credito creada por ese usuario existe y si existe tomo esa tarjeta como objeto y la mando al template
    if(CreditCard.objects.filter(user_id=request.user.id).exists()):
        user_credit_card = CreditCard.objects.get(user_id=request.user.id)
        context = {
            'user_credit_card':user_credit_card,
        }

    else:
        # si no existe envio la variable vacia
        context = {
            'user_credit_card':None,
        }

    return render(request,'users/home.html',context)
    





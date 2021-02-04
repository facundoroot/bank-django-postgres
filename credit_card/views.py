from django.shortcuts import render,redirect
# importo el form para register la tarjeta que cree en .forms
from .forms import CreditCardForm
# importo mensajes
from django.contrib import messages
# importo credit card y user asi chequeo si el usuario ya tiene una tarjeta registrada o no
from credit_card.models import CreditCard
# importo el form que cree para el deposito
from .forms import MoneyActionsForm
from .forms import TransferenceForm
# importo User para poder chequear si el usuario que quiero mandarle dinero existe
from users.models import User
# importo el decorador login_required
from django.contrib.auth.decorators import login_required
# recordar cambiar el redirect de login_required en settings

# Create your views here.
@login_required
def register(request):
    # chequeo si el usuario tiene registrada una tarjeta a su nombre o no
    # si ya tiene registrada no le dejo registrar otra
    if(CreditCard.objects.filter(user_id=request.user.id).exists()):
        form = "Ya tienes una tarjeta registrada a tu nombre"
    else:
        # o toma la info del post que le llego o  el form solo es el form vacio
        form = CreditCardForm(request.POST or None)
        if(form.is_valid()):
            card_number = form.cleaned_data['card_number']
            funds = form.cleaned_data['funds']
            user_id = request.user
            new_cc = CreditCard(user_id=user_id,card_number=card_number,funds=funds)
            new_cc.save()
            messages.success(request,f' your credit card has been registered')
            return redirect('home')


    return render(request,'credit_card/register.html',{'form':form})

@login_required
def deposit(request):
    if(request.method == 'POST'):
        # agarro los valores del form
        form = MoneyActionsForm(request.POST)
        if(form.is_valid()):
            money_amount = form.cleaned_data['money_amount']
            # agarro la credit card de la persona logeada
            user_credit_card = CreditCard.objects.get(user_id=request.user.id)
            user_credit_card.funds = user_credit_card.funds + money_amount
            user_credit_card.save(update_fields=['funds'])
            messages.success(request,f' deposit succesfull')
            return redirect('home')

    else:
        form = MoneyActionsForm()
    
    return render(request,'credit_card/money_actions.html',{'form':form})


@login_required
def withdrawl(request):
    if(request.method == 'POST'):
        form = MoneyActionsForm(request.POST)
        if(form.is_valid()):
            money_amount = form.cleaned_data['money_amount']
            user_credit_card = CreditCard.objects.get(user_id=request.user.id)
            # veo que la cantidad que quiero retirar no sea mayor a la cantidad de dinero que tengo en la cuenta
            if(money_amount <= user_credit_card.funds):
                user_credit_card.funds = user_credit_card.funds - money_amount
                user_credit_card.save(update_fields=['funds'])
                messages.success(request,f' withdrawl succesfull')
                return redirect('home')
            else:
                messages.success(request,f' you cant withdrawl more money than you have in your account')
                return redirect('home')

    else:
        form = MoneyActionsForm()
    
    return render(request,'credit_card/money_actions.html',{'form':form})


@login_required
def transference(request):
    if(request.method == 'POST'):
        form = TransferenceForm(request.POST)
        
        if(form.is_valid()):
            money_amount = form.cleaned_data['money_amount']
            transference_to_name = form.cleaned_data['transfered_to']
            # transfered from es la persona logeada
            transfered_from = request.user

            # veamos si la persona que quiero transferir existe
            if(User.objects.filter(username=transference_to_name).exists()):
                transfered_to = User.objects.get(username=transference_to_name)
                transfered_to_id = transfered_to.id

                # primero vamos a ver que la cantidad de dinero que quiero transferir no sea mayor a la de mi cuenta
                user_credit_card = CreditCard.objects.get(user_id=request.user.id)
                if(money_amount <= user_credit_card.funds):
                    # resto el dinero de la cuenta de la que transfiero el dinero
                    user_credit_card.funds = user_credit_card.funds - money_amount
                    user_credit_card.save(update_fields=['funds'])
                    #sumo dinero a los funds de la cuenta de la persona a la que transfiero
                    user_to_transfer_cc = CreditCard.objects.get(user_id=transfered_to_id)
                    user_to_transfer_cc.funds = user_to_transfer_cc.funds + money_amount
                    user_to_transfer_cc.save(update_fields=['funds'])

                    # mensaje de exito
                    messages.success(request,f'The transference was succesful!')
                    return redirect('transference')

                else:
                    messages.success(request,f' you cant withdrawl more money than you have in your account')
                    return redirect('transference')

            else:
                messages.success(request,f'the username doesent exist, try again')
                return redirect('transference')

        else:
            messages.success(request,f'the username doesent exist, try again')
            return redirect('transference')

    else:
        form = TransferenceForm()

    return render(request,'credit_card/transference.html',{'form':form})






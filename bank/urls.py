"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# importo todas las views
from users import views as user_views
# importo el view de login que ya trae armado django
from django.contrib.auth import views as authentication_views
# importo las views de credit card
from credit_card import views as credit_card_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    # esta view de login la trae echa el as_view se agrega siempre que estemos trabajando con un view preecho de django
    # estos views que trae echos no necesitan en si templates enteros pero si necesitamos crear templates para que funcionen
    # el path para el template se lo agregamos adentro de as_view
    path('',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # recordar cambiar el redirect automatico que hace la pagina al logearse
    # LOGIN_REDIRECT_URL='users:home'
    path('home/',user_views.index,name='home'),
    path('credit_card/register/',credit_card_views.register,name='credit_card_register'),
    path('credit_card/deposit/',credit_card_views.deposit,name='deposit'),
    path('credit_card/withdrawl/',credit_card_views.withdrawl,name='withdrawl'),
    path('credit_card/transference/',credit_card_views.transference,name='transference'),

]

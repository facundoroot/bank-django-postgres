# 1.importo los forms para luego poder usarlo para agregar mas fields
from django import forms
# 2.importo el form de creacion de usuario que ya trae django
from django.contrib.auth.forms import UserCreationForm
# 3.importo el modelo que se conecta a la abse de datos que tambien debere hacerle modificaciones
from django.contrib.auth.models import User



# 4. armo la class form, que extiende de UserCreationForm y agrego los fields que quiero
class RegisterForm(UserCreationForm):
    # UserCreationForm trae de por si los fields,user,password y password2, asi que le agrego los que quiero
    #username
    #password1
    #password2
    email = forms.EmailField()


    # ahora uso una meta class para agregar los fields a UserCreationForm
    # Meta class lo que hace es guardar informacion de la clase en la que se encuentra en este caso RegisterForm
    class Meta:
        # primero especifico a que modelo se le van a agregar los fields en cuanto a la base de datos
        model = User 
        # ahora especifico los fields que van a estar presentes en esta form
        fields = ['username','email','password1','password2']
    

    

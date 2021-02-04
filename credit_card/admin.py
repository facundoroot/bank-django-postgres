from django.contrib import admin
# importo los modelos para que aparezcan en admin
from credit_card.models import CreditCard

# Register your models here.
admin.site.register(CreditCard)

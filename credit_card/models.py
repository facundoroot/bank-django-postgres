from django.db import models
# importo el modelo user ya que voy a crear una foreign key
from django.contrib.auth.models import User

# Create your models here.
class CreditCard(models.Model):
    # armo la foreign key
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    card_number = models.IntegerField()
    funds = models.IntegerField()

class Transference(models.Model):
    # armo la foreign key 
    transfered_from = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    transfered_to = models.CharField(max_length=100)
    money_amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


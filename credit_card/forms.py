from django import forms
from .models import CreditCard
from .models import Transference


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number','funds']

class MoneyActionsForm(forms.Form):
    money_amount = forms.IntegerField()

class TransferenceForm(forms.ModelForm):
    class Meta:
        model = Transference
        fields = ['money_amount','transfered_to']


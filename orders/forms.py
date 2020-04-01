from django import forms
from localflavor.ua.forms import UAPostalCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = UAPostalCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code',
                  'city']

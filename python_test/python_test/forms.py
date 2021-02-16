from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    contact = forms.CharField(required=False)
    address_street = forms.CharField(required=False, label="Street")
    address_suburb = forms.CharField(required=False, label="Suburb")
    address_postcode = forms.CharField(required=False, label="Postcode")
    address_state = forms.CharField(required=False, label="State")
    class Meta:
        model = Client
        fields = ('name','contact','email','phone','address_street','address_suburb','address_postcode','address_state')
        labels = { 'name': 'Client', 'email': 'Email', 'phone': 'Phone'}

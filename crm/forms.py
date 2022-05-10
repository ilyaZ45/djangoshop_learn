from django import forms


class Orderform(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput())
    phone = forms.CharField(max_length=200)

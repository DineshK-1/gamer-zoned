from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from Accounts.models import Profile
from DB.models import Desktop,Laptop

class SignUpForm(UserCreationForm):
    FirstName = forms.CharField(max_length=100,error_messages = { 
                 'required':"Please Enter First Name"
                 }
                 )
    LastName = forms.CharField(max_length=100,error_messages = { 
                 'required':"Please Enter Last Name"
                 })
    email = forms.EmailField(max_length=150,error_messages = { 
                 'required':"Email ID is required!"
                 })
    Address = forms.CharField(max_length=100,
    widget=forms.Textarea(),error_messages = { 
                 'required':"Address is required!"
                 })
    Seller = forms.BooleanField(required=False)
    class Meta():
        model = User
        fields = ('username','FirstName','LastName', 'email', 'password1', 'password2', 'Address', 'Seller')
        error_messages = {
            'username' : {
                'required' : ("Username is required!")
            } ,
            'password1': {
                'required' : ("Password is Required :(")
            },
            'password2': {
                'required' : ("Password Confirmation is Required :(")
            }
        }


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'style':'color:white;'})
        self.fields['FirstName'].widget.attrs.update({'style':'color:white;'})
        self.fields['LastName'].widget.attrs.update({'style':'color:white;'})
        self.fields['username'].widget.attrs.update({'type':''})
        self.fields['FirstName'].widget.attrs.update({'type':''})
        self.fields['LastName'].widget.attrs.update({'type':''})
        self.fields['email'].widget.attrs.update({'style':'color:white;'})
        self.fields['password1'].widget.attrs.update({'style':'color:white;'})
        self.fields['password2'].widget.attrs.update({'style':'color:white;'})
        self.fields['Address'].widget.attrs.update({'style':'color:white;'})
        self.fields['Seller'].widget.attrs.update({'style':'color:white;'})
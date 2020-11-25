from library.models import Profile, Store

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from account.models import CustomUser


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class LoginForm(forms.ModelForm):
    email = forms.CharField(label='Enter your email', max_length=50)
    password = forms.PasswordInput()

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class ProfileRegister(forms.ModelForm):
    address = forms.TextInput()
    town = forms.CharField()
    Date_of_Birth = forms.CharField()
    adhar_card = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['address', 'town', 'Date_of_Birth', 'adhar_card']


class RequestBookForm(forms.Form):
    # name = forms.CharField(max_length=50)
    # email_id = forms.EmailField()
    # address = forms.TextInput()
    # town = forms.CharField()
    # Date_of_Birth = forms.IntegerField()
    # adhar_card = forms.IntegerField()
    #  book_name = forms.CharField(max_length=50)
    #  Copies_required = forms.IntegerField()

    class Meta:
        model = Profile
        fields = ['name','email_id','address', 'town', 'Date_of_Birth', 'adhar_card']  #'book_name','Copies_required'

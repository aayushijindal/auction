from cProfile import label
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from auction.models import *
from datetime import date

class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['firstname'].required = True
    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname', 'email', 'phone']




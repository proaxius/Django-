from django import forms
#login_forms=form_here1
class form_here1(forms.Form):
     username =forms.CharField(max_length=88)
     password =forms.CharField(widget=forms.PasswordInput)
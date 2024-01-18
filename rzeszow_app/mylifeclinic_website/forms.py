from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class SignUpForm(UserCreationForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
        attrs={
            'style': 'width: 300px; margin: 0 auto;',
        }
    ))
            
    first_name = forms.CharField(label="", max_length = 30, widget=forms.TextInput(attrs={'class':'input', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length = 50, widget=forms.TextInput(attrs={'class':'lastName', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'captcha')

    def init(self, args, **kwargs):
        super(SignUpForm, self).init(args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['username'].label = ''
       
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = "<ul class='form-text text-muted small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
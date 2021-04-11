from django import forms
from .models import Users
from .backend import AuthenticationBackend

backend = AuthenticationBackend()


class SignInForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email_address', 'password')
        widgets = {
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control Password', 'placeholder': 'Password'})
        }

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email_address = self.cleaned_data.get('email_address')
        password = self.cleaned_data.get('password')

        if email_address is not None and password:
            self.user_cache = backend.authenticate(email_address=email_address, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email address or password.')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control Password',
                                                                 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control ConfirmPassword',
                                                                  'placeholder': 'Confirm Password'}))

    class Meta:
        model = Users
        fields = ('email_address', 'first_name', 'last_name', 'password', 'confirm_password')
        widgets = {
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        }

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match."
            )
        return data

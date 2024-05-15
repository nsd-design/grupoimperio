from crispy_forms.helper import FormHelper
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

from grupo_app.models import CouponCode


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur ",
        max_length=20, required=True,
    )
    password = forms.CharField(
        label="Mot de passe ",
        max_length=120,
        widget=forms.PasswordInput(),
    )


class RegisterForm(forms.Form):
    lastname = forms.CharField(
        label="Nom",
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "e.g: doe"})
    )
    firstname = forms.CharField(label="Prénom", max_length=80, required=True,
                                widget=forms.TextInput(attrs={"placeholder": "e.g: smith"}))
    email = forms.EmailField(label="Email", required=True,
                             widget=forms.EmailInput(attrs={"placeholder": "smithdoe@example.com"}))
    username = forms.CharField(label="Nom d'utilisateur", max_length=20, required=True,
                               widget=forms.TextInput(attrs={"placeholder": "e.g: smith"}))
    password = forms.CharField(label="Mot de passe", max_length=120, min_length=8,
                               widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirmation du mot de passe", max_length=120,
                                       widget=forms.PasswordInput(), min_length=8)
    telephone = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget())


class CouponCodeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CouponCodeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["coupon"].label = "Entrez le code coupon "

    class Meta:
        model = CouponCode
        fields = ["coupon"]

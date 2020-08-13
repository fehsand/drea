from django import forms
from .models import iletisim

class iletisimForm(forms.ModelForm):

    class Meta:
        model = iletisim
        fields = ('isim', 'soy_isim', 'eposta', 'telefon', 'mesaj',)
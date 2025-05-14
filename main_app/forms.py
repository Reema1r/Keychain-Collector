from django.forms import ModelForm
from .models import KeychainImage

class KeychainImageForm(ModelForm):
    class Meta:
        model = KeychainImage
        fields = ["image","caption"]
        
from django.forms import ModelForm
from .models import Reprint

class ReprintForm(ModelForm):
    class Meta:
        model = Reprint
        fields = ['date', 'edition_type']
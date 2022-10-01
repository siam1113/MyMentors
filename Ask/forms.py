from django.db.models import fields
from django.forms import ModelForm
from .models import Ask
class AskForm(ModelForm):
    class Meta:
        model = Ask
        fields = '__all__'
        exclude=['datetime']

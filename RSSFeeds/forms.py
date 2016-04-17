from django import forms

from .models import Feeds

class FeedsForm(forms.ModelForm):
    class Meta:
        model = Feeds
        fields = ('url',)

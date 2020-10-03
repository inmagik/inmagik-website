from django import forms
from .models import SiteCheckup

class SiteCheckupForm(forms.ModelForm):
    class Meta:
        model = SiteCheckup
        fields = "__all__"

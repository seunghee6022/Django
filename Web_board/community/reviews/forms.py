from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'


#pip install django_bootstrap4
#pip install -e 해줘야
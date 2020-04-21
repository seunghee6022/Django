from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'


#pip install django_bootstrap4
#pip install -e 해줘야

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
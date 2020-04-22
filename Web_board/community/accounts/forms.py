from django.contirb.auth import get_user_momdel
from django.contirb.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model
        fields = '__all__'


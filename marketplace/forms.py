from django.contrib.auth.forms import UserCreationForm
from marketplace.models import User



class RegForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
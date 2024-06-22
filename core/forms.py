from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        



class CustomUserChangeForm(UserChangeForm):
    '''This form is for user update in django admin'''

    class Meta:
        model = User

        exclude = ('password',)
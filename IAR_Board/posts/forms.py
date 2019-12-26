from django.forms import ModelForm
from .models import AddPost

class AddPostForm(ModelForm):
    class Meta:
        model = AddPost
        fields = ['postingTitle', 'city', 'postalCode', 'description', 'email', 'phoneNumber']
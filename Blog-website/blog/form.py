from django.forms import ModelForm
from .models import Post
class ProjectForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
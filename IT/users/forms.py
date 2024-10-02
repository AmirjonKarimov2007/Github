from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CystomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Ism',
            'last_name':'Familiya',
            'email':'Elektron Maznil',
            'username':'Login'
            
        }

    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)

        for key, field in self.fields.items():
            # print(f"key:{key}\nfield:{field}")
            field.widget.attrs.update({"class": "input input--text"})
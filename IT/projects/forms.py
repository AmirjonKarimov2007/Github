from django.forms import ModelForm
from .models import Project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'tag': forms.CheckboxSelectMultiple()
        }


    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)

        for key, field in self.fields.items():
            # print(f"key:{key}\nfield:{field}")
            field.widget.attrs.update({"class": "input input--text"})
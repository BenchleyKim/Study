from django.forms import ModelForm, fields
from community.models import *

class Form(ModelForm) :
    class Meta :
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']

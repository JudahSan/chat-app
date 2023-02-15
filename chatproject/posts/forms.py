from .models import Post
from django import forms 
from crispy_forms.helper import FormHelper

class PostCreateForm(forms.ModelForm):
  class Meta:
    model = Post 
    fields =  ('title', 'image', 'caption')


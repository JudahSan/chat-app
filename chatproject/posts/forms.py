from .models import Post
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class PostCreateForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.add_input(Submit('submit', 'Submit'))


  class Meta:
    model = Post 
    fields =  ('title', 'image', 'caption')


from .models import Post, Comment
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class PostCreateForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.add_input(Submit('submit', 'Submit'))

    self.fields['message'].widget.attrs['placeholder'] = 'Comment'


  class Meta:
    model = Post 
    fields =  ('title', 'image', 'caption')

# Comment form
class CommentForm(forms.ModelForm):
  class Meta: 
    model = Comment 
    fields = ('message', 'post_by' )
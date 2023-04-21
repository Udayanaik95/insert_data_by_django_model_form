from django import forms
from App.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        labels={'topic_name':'Topic Name','name':'Name'}
        #widgets={'name':forms.PasswordInput,'url':forms.Textarea}
        help_texts={'topic_name':'Should not be integer','name':'Only Alphabet'}

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
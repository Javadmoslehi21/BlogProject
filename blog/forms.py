from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from .models import Message

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='Your name', widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(max_length=1000, label='Your Message', widget=forms.Textarea(attrs={"class": "form-control"}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "form-control"}))


    def clean(self):
        name  = self.cleaned_data.get('name')
        text  = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('Name and Text are same', code='Fields_same')
      
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if name.isnumeric():
    #         raise ValidationError('not number in name', code='num')
    #     return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'inter your title'}),
            'text': forms.Textarea(attrs={'class':'form-control','placeholder':'inter your text'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'inter your text'}),
        }
from django import forms
from django.forms import ModelForm

from posts.models import Post, Category


class PostForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : 'form-control', 'rows': '20'}))
    category = forms.ModelChoiceField(label='', queryset=Category.objects.all(), initial=0)

    class Meta:
        model = Post
        fields = ['title', 'description', 'category']
        # widgets = {
        #     'description': forms.Textarea(attrs={'class' : 'form-control', 'label': ""}),
        # }

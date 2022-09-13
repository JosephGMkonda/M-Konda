from django import forms
from Feeds.models import Posts

class newPost(forms.ModelForm):
    caption = forms.CharField(
        widget=forms.Textarea
        (attrs={'class':'input is-medium', 
        'rows':4, 'cols':70,"placeholder":'What is your mind ?'}),
        label='', required=False)

    pictures = forms.ImageField(label='',required=False)

    class Meta:
        model = Posts
        fields = ['caption','pictures']
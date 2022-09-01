from django import forms
from Feeds.models import Posts

class newPost(forms.ModelForm):
    caption = forms.CharField(widget=forms.Textarea(attrs={'class':'input is-medium'}), required=False)
    pictures = forms.ImageField(required=False)

    class Meta:
        model = Posts
        fields = ['caption','pictures']
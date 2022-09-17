from socket import fromshare
from django import forms
from comment.models import comments

class CommentForms(forms.ModelForm):
    body = forms.CharField( 
        label="",
        widget=forms.Textarea

        (attrs=
        {
            'class':'input is-medium',
            'rows':'2',
            'cols':'70',
            'placeholder':'write your comment'
        
        }),
        required=True)

    class Meta:
        model = comments
        fields = ('body',)
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'commentaire']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control text-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control text-input'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control text-area', 'row': 4})
        } 
        labels = {
            'name': 'NOM',
            'email': 'E-MAIL',
            'commentaire': 'COMMENTAIRE'
        }
    

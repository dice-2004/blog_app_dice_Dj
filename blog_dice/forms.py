from django import forms
from blog_dice.models import

class CommentForm(forms.ModelForm):
    class Meta:
        model = ""
        fields = ["name","body"]

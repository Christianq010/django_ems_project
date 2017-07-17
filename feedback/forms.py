from django import forms
from .models import Feedback

# Our new form
class FeedbackAddForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols': 40,'style': 'resize:none;'}))    
    
    class Meta:
        model = Feedback
        fields = ('name', 'subject', 'category', 'email', 'comment', 'is_read',)


# Our form to edit
class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols': 40,'style': 'resize:none;'}))
    created_on = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': '38'}))

    class Meta:
        model = Feedback
        fields = '__all__'

from django import forms
from .models import Feedback

# import for form validation
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

# Our new form
class FeedbackAddForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 20}), validators=[EmailValidator(), MinLengthValidator(7), MaxLengthValidator(25, message="This is too long")])
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

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols': 40,'style': 'resize:none;'}))

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackAdmin(ModelAdmin):
    form = FeedbackForm
    search_fields = ('name', 'category', 'email', 'subject')
    list_display = ('name', 'category', 'email', 'subject', 'is_read')
    list_editable = ('is_read',)

admin.site.register(Feedback, FeedbackAdmin)
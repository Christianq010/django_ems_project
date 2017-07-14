from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackAdmin(ModelAdmin):
    form = FeedbackForm
    list_display = ('name', 'category', 'email', 'subject', 'is_read')


admin.site.register(Feedback, FeedbackAdmin)
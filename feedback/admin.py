from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Feedback
from .forms import FeedbackForm, FeedbackAddForm
from .actions import mark_feedback_as_read



class FeedbackAdmin(ModelAdmin):
    form = FeedbackForm
    search_fields = ('name', 'category', 'email', 'subject')
    list_display = ('name', 'category', 'email', 'subject', 'is_read')
    list_editable = ('is_read',)
    # readonly_fields = ('created_on',)
    # button placement
    # save_on_top = True
    # actions_on_bottom = False
    actions = [mark_feedback_as_read]

# below to place standard size for all text-areas etc
    """
    formfield_overrides = {
    models.CharField{widget=forms.Textarea(attrs={'rows':6,'cols': 40,'style': 'resize:none;'})}
    models.CharField{widget=forms.TextInput(attrs={'readonly': 'readonly', 'size': '38'})}
    }
    """

# This function returns original form when a new form is requested
# Returns another when requesting for a edit for a form that exists
    def get_form(self, request, obj=None, **kwargs): 

        if obj is None:
            return FeedbackAddForm
        else: 
            return super(FeedbackAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Feedback, FeedbackAdmin)

# Custom dropdown action
def mark_feedback_as_read(modeladmin, request, queryset):
    for employeeFeedback in queryset:
        employeeFeedback.is_read = True
        employeeFeedback.save()
    # add message pop up
    modeladmin.message_user(request,"%s successfully marked as read" % len(queryset))


# rename our custom selection
mark_feedback_as_read.short_description = "Mark selected as read"

from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    
    CATEGORY_CHOICES = (
        ('1', 'General'),
        ('2', 'Management'),
        ('3', 'Compensation'),
        ('4', 'Suggestions'),
        ('5', 'Complaint'),                                                                                
    )

    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=10, default='1', choices=CATEGORY_CHOICES)
    email = models.CharField(max_length=150)
    comment = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.email

    class Meta:
        # this is the table name
        db_table = 'feedback'

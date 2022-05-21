from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Need to check this

    
class Bug(models.Model):
    # User and bugs created get deleted when remove
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.TextField() # Check this TestField max_length?
    # Other ways to do this (priority), first test
    PRIORITY_CHOICES = [('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')]
    priority = models.CharField(max_length=6, choices= PRIORITY_CHOICES, default='LOW')
    
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.bug_text
    
    
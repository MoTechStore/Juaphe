from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import os
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'



class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)
        
class Task(models.Model):
    task_title = models.CharField(max_length=100,blank=True, null=True)
    task_customer = models.CharField(max_length=100,blank=True, null=True)
    supervisor = models.CharField(max_length=100,blank=True, null=True)
    task_desc = models.CharField(max_length=100,blank=True, null=True)
    amount = models.CharField(max_length=100,blank=True, null=True)
    modus = models.CharField(max_length=10000,blank=True, null=True)
    comment = models.CharField(max_length=100,blank=True, null=True)
    suspect = models.CharField(max_length=100,blank=True, null=True)
    status = models.CharField(max_length=100,blank=True, null=True)
    days_counter = models.IntegerField(blank=True, null=True)
    task_days = models.IntegerField(blank=True, null=True)
    exceed_days = models.IntegerField(blank=True, null=True)
    task_deadline = models.DateTimeField(null=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.FileField(upload_to='document/report/', null=True, blank=True)
    invoice = models.FileField(upload_to='document/invoice/', null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)


    def __str__(self):
        return self.task_title

    def delete(self, *args, **kwargs):
        self.report.delete()
        self.invoice.delete()
        super().delete(*args, **kwargs)

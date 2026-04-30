from django.db import models
from projects.models import Project
from django.conf import settings

class Task(models.Model):
    STATUS_CHOICES = [
        ("TD", "TODO"),
        ("IP", "IN_PROGRESS"),
        ("DO", "DONE"),
    ]
    
    PRIORITY_CHOICES = [
        ("LW", "LOW"),
        ("ME", "MEDIUM"),
        ("HI", "HIGH"),
    ]
    
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True)
    status = models.CharField(default="TD", max_length=2, choices=STATUS_CHOICES)
    priority = models.CharField(default="ME", max_length=2, choices=PRIORITY_CHOICES)
    deadline = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="created_tasks", on_delete=models.CASCADE)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="assigned_tasks", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
class Comment(models.Model):
    text = models.TextField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owned_projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProjectMember(models.Model):
    ROLES = [
        ("OW", "OWNER"),
        ("MR", "MANAGER"),
        ("ME", "MEMBER"),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLES)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'project'],
                name='unique_project_member',
            )
        ]
    
    
    
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    subscribe_to_jobs = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class JobPosting(models.Model):
    company_name = models.CharField(max_length=200)
    job_url = models.URLField()

    def __str__(self):
        return f"{self.company_name} - Job Posting" 
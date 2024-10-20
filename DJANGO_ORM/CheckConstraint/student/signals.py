from django.db.models.signals import pre_delete, post_delete
from .models import Student
from django.dispatch import receiver

@receiver(pre_delete, sender=Student)
def pre_delete_profile(sender, **kwargs):
    print("You are about to delete a student!")

@receiver(post_delete, sender=Student)
def post_delete_profile(sender, **kwargs):
    print("You have deleted a student!!!")
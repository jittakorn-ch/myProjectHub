from django.db import models

class TodoList(models.Model):
    todo_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=256)
    description = models.CharField(max_length=512, blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False, help_text="False=Incomplete, True=Completed")  # Fix default value
    date_created = models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.
class Task(models.Model):
    tasktitle=models.CharField(max_length=30)
    teskdesc=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.tasktitle

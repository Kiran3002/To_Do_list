from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    completed_at=models.DateTimeField(null=True,blank=True)
    image=models.ImageField(upload_to='task_images' , null=True,blank=True)

    def __str__(self):
        return self.title
class Contactus(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(blank=False,null=False)
    phone=models.CharField(max_length=10,blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    created_us=models.DateTimeField(auto_now_add=True)
    is_addressed=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
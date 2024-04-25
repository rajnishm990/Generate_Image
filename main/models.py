from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='static/images/')
    prompt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt
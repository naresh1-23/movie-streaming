from django.db import models


class Videos(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    rating = models.IntegerField(null = True, blank=True)
    video_url = models.FileField(upload_to = "movies/", null=True, blank = True)
    thumbnail = models.ImageField(upload_to = "thumbnail/", null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    count_of_files = models.IntegerField(default=0)

    def __str__(self):
        return self.name

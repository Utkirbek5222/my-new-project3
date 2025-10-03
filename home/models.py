from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    curse = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subjects_tutor = models.CharField(max_length=255)
    description = models.TextField()
    detail = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="step/")
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


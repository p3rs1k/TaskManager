from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"

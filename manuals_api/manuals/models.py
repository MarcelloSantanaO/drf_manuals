from django.db import models


class Manual(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    link = models.URLField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Practices(models.Model):
    RELEVANCE_CHOICES = {
        ('MINIMAL', '1'),
        ('MEDIUM', '2'),
        ('HIGH', '3')
    }
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=255, null=False, blank=False)
    relevance = models.CharField(max_length=50, choices=RELEVANCE_CHOICES, null=False, blank=False)
    reference = models.ManyToManyField(Manual)

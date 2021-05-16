from django.db import models
from random import randint


# Create your models here.
class Document(models.Model):
    doc_name = models.CharField(verbose_name="document_name", default=f"Document{randint(1029283, 918829102832123)}",
                                max_length=120, blank=True, unique=True)
    doc = models.TextField(verbose_name="document")
    about = models.TextField(help_text="Write some description about the document", default="", blank=True)
    doc_img = models.ImageField(default="doc_image.png", verbose_name="document_img")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length = 512)
    keywords = models.CharField(max_length = 512)
    description = models.CharField(max_length = 1000)
    company = models.CharField(max_length = 512)
    address = models.CharField(blank = True, max_length = 512)
    phone = models.CharField(max_length = 12)
    fax = models.CharField(blank = True, max_length = 20)
    email = models.EmailField(max_length = 512)
    smtpserver = models.CharField(blank = True, max_length = 512)
    smtpemail = models.CharField(blank=True,max_length = 512)
    smtppassword = models.CharField(blank=True,max_length = 512)
    smtpport = models.CharField(blank=True,max_length = 20)
    icon = models.ImageField(blank=True,upload_to = 'images/')
    facebook = models.CharField(blank=True,max_length = 50)
    instagram = models.CharField(blank=True,max_length = 50)
    twitter = models.CharField(blank=True,max_length = 50)
    youtube = models.CharField(blank=True, max_length = 50)
    aboutus = RichTextUploadingField(blank = True)
    contact = RichTextUploadingField(blank = True)
    references = RichTextUploadingField(blank = True)
    status = models.CharField(max_length=10,choices = STATUS)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
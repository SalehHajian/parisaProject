from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('drf' , 'Draft') ,
        ('pub' , 'Published')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES , max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])
from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='news_covers/')
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

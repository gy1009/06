from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Shop(models.Model) :
    title = models.CharField(max_length=100, verbose_name="书店名")
    description = models.TextField(verbose_name="书店简介")
    image = models.ImageField(upload_to='shop/images/', verbose_name="书店封面" )
    url = models.URLField(blank=True, verbose_name="书店链接")

    class Meta:
        verbose_name = "书店"
        verbose_name_plural = "书店"
    def __str__(self):
        return self.title
class Review(models.Model):
        text = models.CharField(max_length=100)
        date = models.DateTimeField(auto_now_add=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_reviews')
        shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
        watchAgain = models.BooleanField()
        def __str__(self):
                return self.text
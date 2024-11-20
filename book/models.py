from django.db import models
from django.contrib.auth.models import User

class Book(models.Model) :
    title = models.CharField(max_length=100,verbose_name="书籍名")
    description = models.CharField(max_length=250,verbose_name="书籍简介")
    image = models.ImageField(upload_to='book/images/',verbose_name="书籍封面" )
    url = models.URLField(blank=True,verbose_name="书籍资源链接")
    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = "书籍"
    def __str__(self):
        return self.title
class Review(models. Model) :
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self) :
        return self.text


# Create your models here.

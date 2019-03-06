from django.db import models


# Create your models here.

class Gallery(models.Model):
    # CharField()创建文本区域，最大长度100
    description = models.CharField(default='在这里写作品的简介', max_length=100)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='作品标题', max_length=30)

    def __str__(self):
        return self.title

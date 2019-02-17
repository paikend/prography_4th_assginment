from django.db import models
from django.contrib.auth import get_user_model

#1.함수를 이용해서 찾기
#2. 유저 모델을 불러와서 사용하는 방법
# from django.contrib.auth.models import User
# 3,세팅 파일에 있는 설정을 불러와서 사용하는 방법 :  'auth.user'

# Create your models here.
from django.urls import reverse_lazy
from tagging.fields import TagField


class Photo(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image =  models.ImageField(upload_to='images/%y/%m/%d/', blank=True )
    tag = TagField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def get_absolute_url(self):
        return reverse_lazy('photo:photo_detail', args=[self.id])

    def __str__(self):
        return self.writer.username+ " " + self.created.strftime("%Y-%m-%d %H:%M:%S")


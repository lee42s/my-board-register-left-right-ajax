from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField('Content', blank=True)
    # https://goo.gl/GKVaAa 처음 생성될때 자동으로 현재 시간을 설정
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    # https://goo.gl/GKVaAa 매번 저장될때 자동으로 현재 시간을 설정
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, null=True)
        
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table  = 'board_posts'
        ordering  = ('-create_date',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse에서 인자로 리스트를 전달하고자 하는 경우는 args=[1,5]
        return reverse('board:post_detail', kwargs={'pk':self.id})

    def get_previous_post(self):
        # get_previous_by_<필드명> 메서드
        try:
            return self.get_previous_by_create_date()
        except Post.DoesNotExist:
            return None

    def get_next_post(self):
        # get_next_by_<필드명> 메서드
        try:
            return self.get_next_by_create_date()
        except Post.DoesNotExist:
            return None
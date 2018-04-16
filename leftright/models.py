from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    LATE = 'LT'
    LEFT = 'LF'
    RIGHT = 'RT'
    GAME_TYPE = ((LEFT, '왼쪽'), (RIGHT, '오른쪽'),)

    leftright = models.CharField(
        max_length=2,
        choices=GAME_TYPE,
        default='LT',
    )
    usr = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.leftright
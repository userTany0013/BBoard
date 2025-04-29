from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

tanks = 'TAN'
healers = 'HEL'
dd = 'D_D'
merchants = 'MER'
guild_masters = 'GUM'
quest_givers = 'GUG'
blacksmiths = 'BLS'
tanners = 'TNS'
potion_makers = 'POT'
spellmasters = 'SPL'

CAT = [
    (tanks, 'Танки'),
    (healers, 'Хилы'),
    (dd, 'ДД'),
    (merchants, 'Торговцы'),
    (guild_masters, 'Гилдмастеры'),
    (quest_givers, 'Квестгиверы'),
    (blacksmiths, 'Кузнецы'),
    (tanners, 'Кожевники'),
    (potion_makers, 'Зельевары'),
    (spellmasters, 'Мастера заклинаний'),
]


consideration = 'CN'
adopted = 'AD'
rejected = 'RE'

STA = [
    (consideration, 'Рассмотрение'),
    (adopted, 'Принят'),
    (rejected, 'Отклонён'),
]


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts')
    category = models.CharField('Категория', max_length=3, choices=CAT)
    date_time = models.DateTimeField('Дата и время', auto_now=True)
    heading = models.CharField('Заголовок', max_length=250)
    text = models.TextField('Текст')


class Responses(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True, related_name='responses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='responses')
    date_time = models.DateTimeField('Дата и время', auto_now=True)
    text = models.TextField('Текст')
    status = models.CharField('Статус', max_length=2, choices=STA)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers, send_mail

from .models import Responses, Posts


@receiver(post_save, sender=Responses)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        id = instance.id
        res = Responses.objects.get(id=id)
        ps = Posts.objects.get(id=res.post.id)
        to = ps.user.email
        post = instance.post.heading
        message = f'Оставлен отклик о вашем посте : {post}'
        send_mail(
            subject='Отклик',
            message=message,
            from_email="Tany911922@yandex.ru",
            recipient_list=[to, ],
        )
    else:
        to = instance.user.email
        post = instance.post.heading
        message = f'Автор изменил статус вашего отклика на пост : {post}'
        send_mail(
            subject='Отклик',
            message=message,
            from_email="Tany911922@yandex.ru",
            recipient_list=[to, ],
        )
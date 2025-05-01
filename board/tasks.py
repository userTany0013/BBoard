from django.contrib.auth.models import User
from datetime import datetime, timedelta

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from board.models import Posts


def send_mail():
    date = datetime.now()
    new_date = date - timedelta(weeks=1)
    to = []
    users = User.objects.all()
    for user in users:
        to.append(user.email)

    post_list = []
    posts = Posts.objects.all()
    for post in posts:
        if post.date_time > new_date:
            post_list.append(post)
    html_content = render_to_string(
        'week.html',
        {
            'post_list': post_list
        }
    )
    msg = EmailMultiAlternatives(
        subject='Рассылка',
        from_email='Tany911922@yandex.ru',
        to=to
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

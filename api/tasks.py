from time import sleep
from django.core.mail import send_mail
from rainbow6siege_api.celery import app


@app.task
def send_email_task(user_email, message):
    sleep(1)
    print('done')
    send_mail(
        'Отправлено',
        message,
        'mr.world008@gmail.com',
        [user_email]
    )

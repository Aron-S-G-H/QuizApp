from django.db import models

# Create your models here.


class Question(models.Model):
    CHOISES = [
        ('option1', 'option1'),
        ('option2', 'option2'),
        ('option3', 'option3'),
        ('option4', 'option4'),
    ]
    question = models.CharField(max_length=50, unique=True)

    option1 = models.CharField(max_length=50)

    option2 = models.CharField(max_length=50)

    option3 = models.CharField(max_length=50)

    option4 = models.CharField(max_length=50)

    answer = models.CharField(max_length=10, choices=CHOISES)

    status = models.BooleanField(default=False, help_text='وضعیت انتشار سوال')

    def __str__(self):
        return self.question


class UserResult(models.Model):
    fullname = models.CharField(max_length=20)

    totall = models.PositiveSmallIntegerField(default=0)

    score = models.PositiveSmallIntegerField(default=0)

    percent = models.FloatField(max_length=5)

    correct = models.PositiveSmallIntegerField(default=0)

    wrong = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

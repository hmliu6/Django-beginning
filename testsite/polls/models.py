from django.db import models

# Create your models here.

class question(models.Model):

    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('Date published')

    def __str__(self):
        return self.questionText

class choice(models.Model):

    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choiceText
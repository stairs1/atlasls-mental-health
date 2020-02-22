from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):

    user = models.ForeignKey(User, related_name="surveys", on_delete=models.CASCADE)
    ordinal = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"user: {self.user} | survey #{self.ordinal} | timestamp: {self.timestamp}"
        )


class Answer(models.Model):

    user = models.ForeignKey(User, related_name="answers", on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, related_name="answers", on_delete=models.CASCADE)
    question_ordinal = models.IntegerField()
    answer = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"user: {self.user} | question #{self.question_ordinal} | answer: {self.answer} | timestamp: {self.timestamp} | Survey info -->: {self.survey}"

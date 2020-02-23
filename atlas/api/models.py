from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


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


class JournalStub(models.Model):

    title = models.CharField(max_length=300)
    authors_date = models.CharField(max_length=300)
    relevant_questions = models.CharField(max_length=12)
    summary = models.CharField(max_length=2000)
    subject_group = models.CharField(max_length=2000)
    other_findings = models.CharField(max_length=2000)
    task_mindfullness = models.CharField(max_length=2000)
    task_wellness = models.CharField(max_length=2000)
    task_clinical = models.CharField(max_length=2000)


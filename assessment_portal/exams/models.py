from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'mc'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default=TEXT)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Exam(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)
    duration_minutes = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Submission(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    text_answer = models.TextField(blank=True, null=True)

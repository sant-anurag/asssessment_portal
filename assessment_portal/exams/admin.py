from django.contrib import admin
from .models import Exam, Question, Choice, Submission, Answer

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Answer)
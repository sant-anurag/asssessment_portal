from django.shortcuts import render, get_object_or_404
from .models import Exam, Submission, Answer, Question, Choice

from django.shortcuts import render


def home(request):
    exams = Exam.objects.all()  # Fetch all available exams
    return render(request, 'exams/home.html', {'exams': exams})



def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    if request.method == "POST":
        submission = Submission.objects.create(exam=exam, user=request.user)
        for question in exam.questions.all():
            if question.question_type == Question.MULTIPLE_CHOICE:
                selected_choice = request.POST.get(f'question_{question.id}')
                choice = Choice.objects.get(id=selected_choice)
                Answer.objects.create(submission=submission, question=question, selected_choice=choice)
            elif question.question_type == Question.TEXT:
                text_answer = request.POST.get(f'question_{question.id}')
                Answer.objects.create(submission=submission, question=question, text_answer=text_answer)

        return render(request, 'exams/submission_complete.html', {'exam': exam})

    return render(request, 'exams/take_exam.html', {'exam': exam})

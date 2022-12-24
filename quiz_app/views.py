from django.shortcuts import render, redirect, reverse
from .models import Question, UserResult
from django.views.generic import View
from django.contrib import messages


# Create your views here.


class Quiz(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_flag = True

            if UserResult.objects.filter(fullname=request.user.username).exists():
                user_flag = False

            questions = Question.objects.all()

            return render(request, 'index.html', {'questions': questions, 'flag': user_flag})
        else:
            return redirect('account:login_page')

    def post(self, request):
        questions = Question.objects.all()
        fullname = request.user.username
        totall = 0
        score = 0
        correct = 0
        wrong = 0
        for q in questions:
            totall += 1
            if q.answer == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (totall * 10) * 100

        UserResult.objects.create(
            fullname=fullname,
            totall=totall,
            score=score,
            percent=percent,
            correct=correct,
            wrong=wrong,
        )

        return redirect(reverse('quiz:result_page') + f'?fullname={fullname}')


class Result(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                fullname = request.GET.get('fullname')
                user_object = UserResult.objects.get(fullname=fullname)
                return render(request, 'quiz_app/result.html', {'user': user_object})
            except:
                return redirect('quiz:quiz_page')
        else:
            return redirect('account:login_page')

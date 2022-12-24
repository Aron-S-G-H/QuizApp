from django.urls import path
from.views import Quiz, Result

app_name = 'quiz'
urlpatterns = [
    path('', Quiz.as_view(), name='quiz_page'),
    path('result', Result.as_view(), name='result_page'),
]

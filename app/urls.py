# urls.py
from django.urls import path
from .views import index, bolim_detail, fan_detail, vazifa_detail, quiz, submit_quiz, quiz_result

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('bolim/<int:bolim_id>/', bolim_detail, name='bolim_detail'),
    path('fan/<int:fan_id>/', fan_detail, name='fan_detail'),
    path('vazifa/<int:vazifa_id>/', vazifa_detail, name='vazifa_detail'),
    path('quiz/<int:vazifa_id>/', quiz, name='quiz'),
    path('submit_quiz/<int:vazifa_id>/', submit_quiz, name='submit_quiz'),
    path('quiz_result/', quiz_result, name='quiz_result'),
]

# views.py
from django.shortcuts import redirect, render, get_object_or_404
from .models import Bolimlar, Fan, Vazifa, Question, Answer

def index(request):
    bolimlar_list = Bolimlar.objects.all()
    return render(request, 'index.html', {'bolimlar_list': bolimlar_list})

def bolim_detail(request, bolim_id):
    bolim = get_object_or_404(Bolimlar, pk=bolim_id)
    fans = Fan.objects.filter(Bolim=bolim)
    return render(request, 'bolim_detail.html', {'bolim': bolim, 'fans': fans})

def fan_detail(request, fan_id):
    fan = get_object_or_404(Fan, pk=fan_id)
    vazifalar = Vazifa.objects.filter(Fan=fan)
    return render(request, 'fan_detail.html', {'fan': fan, 'vazifalar': vazifalar})

def vazifa_detail(request, vazifa_id):
    vazifa = get_object_or_404(Vazifa, pk=vazifa_id)
    questions = Question.objects.filter(nomi=vazifa)
    return render(request, 'vazifa_detail.html', {'vazifa': vazifa, 'questions': questions})

def quiz(request, vazifa_id):
    vazifa = get_object_or_404(Vazifa, pk=vazifa_id)
    questions = Question.objects.filter(nomi=vazifa)
    return render(request, 'quiz.html', {'vazifa': vazifa, 'questions': questions})


def submit_quiz(request, vazifa_id):
    if request.method == 'POST':
        score = 0
        total_questions = 0

        for question in Question.objects.filter(nomi__id=vazifa_id):
            total_questions += 1
            selected_answer_id = request.POST.get(f'question_{question.id}')

            if selected_answer_id:
                selected_answer = Answer.objects.get(pk=selected_answer_id)
                if selected_answer.is_correct:
                    score += 1

        return render(request, 'result.html', {'score': score, 'total_questions': total_questions})
    else:
        return redirect('quiz:quiz_index')

def quiz_result(request):
    return render(request, 'result.html', {})

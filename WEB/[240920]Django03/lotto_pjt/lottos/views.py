from django.shortcuts import render
import random
# Create your views here.

def index(request) :

    lottos = sorted(list(random.sample(range(1,46), 6)))
    real_lottos = [4, 9, 12, 15, 33, 45]
    correct_lottos = list(set(lottos).intersection(real_lottos))
    context = {
        'lottos' : lottos,
        'real_lottos' : real_lottos,
        'correct_lottos' : correct_lottos,
    }
    return render(request, 'lottos/index.html', context)
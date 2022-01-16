import time
import math
from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    game = Game.objects.all()[0]
    game.money += math.ceil(((time.time() - Game.objects.all()[0].last_login) / (60 ** 2))*sum(map(lambda a:a.profitphr,Chef.objects.all())))
    game.last_login = time.time()
    game.save()
    return render(request, 'home.html',context={'game':game,'chefs':Chef.objects.all(),'specialities':Speciality.objects.all()})

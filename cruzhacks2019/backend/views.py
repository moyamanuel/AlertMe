from django.shortcuts import render
from backend.models import Person
# from message import *

# Create your views here.

def index(request):
    if request.method == "POST":
        new_subscriber = Person(
            first_name = request.POST.get('first'),
            last_name = request.POST.get('last'),
            phone_number = request.POST.get('number')
        )
        new_subscriber.save()
        # on_register(new_subscriber['phone_number'])

    return render(request, "backend/index.html")

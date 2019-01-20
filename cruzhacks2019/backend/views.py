from django.shortcuts import render
from backend.models import Person

# Create your views here.

def index(request):
    if request.method == "POST":
        new_subscriber = Person(
            first_name = request.POST.get('first'),
            last_name = request.POST.get('last'),
            phone_number = request.POST.get('number')
        )
        new_subscriber.save()
    return render(request, "backend/index.html")

from django.shortcuts import render
from .models import Document


# Create your views here.
def home_view(request):
    return render(request, "home.html", {'document': Document.objects.all})

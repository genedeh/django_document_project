from django.shortcuts import render
from .models import Document
from django.views.generic import DetailView


# Create your views here.
def home_view(request):
    return render(request, "home.html", {'document': Document.objects.all})


class DocumentDetailView(DetailView):
    model = Document
    template_name = r'C:\Users\Genesis\PycharmProjects\django_practice\document_writer\templates\detail.html'


def new_view(request):
    return render(request, "new.html")

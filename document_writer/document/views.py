from django.shortcuts import render
from .models import Document
from django.views.generic import DetailView


# Create your views here.
def home_view(request):
    return render(request, "home.html", {'document': Document.objects.all})


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document/detail.html'

from django.shortcuts import render, redirect
from .models import Document
from django.views.generic import DetailView
from .forms import DocumentForm


# Create your views here.
def home_view(request):
    return render(request, "home.html", {'document': Document.objects.all})


class DocumentDetailView(DetailView):
    model = Document
    template_name = r'C:\Users\Genesis\PycharmProjects\django_practice\document_writer\templates\detail.html'


def new_view(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("document:home")
    else:
        form = DocumentForm
    return render(request, "new.html", {'form': form})

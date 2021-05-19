from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from django.views.generic import DetailView
from .forms import DocumentForm
from fpdf import FPDF


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
            doc = form.cleaned_data['doc']
            doc_name = form.cleaned_data['doc_name']
            about = form.cleaned_data['about']
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=doc_name,
                     ln=1, align='C')
            pdf.cell(200, 20, txt=doc,
                     ln=2, align='C')
            pdf.cell(200, 10, txt=f"This is the about:{about}", ln=4, align='C')
            pdf.output(f"static/{doc_name}.pdf")
            form.save()
            return redirect("document:home")
    else:
        form = DocumentForm
    return render(request, "new.html", {'form': form})


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Document, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete.html", context)
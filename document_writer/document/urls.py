from django.urls import path
from .views import home_view, DocumentDetailView

app_name = "document"

urlpatterns = [
    path('', home_view, name="home"),
    path('detail/<pk>/', DocumentDetailView.as_view(), name="detail"),
]

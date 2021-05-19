from django.urls import path
from .views import home_view, DocumentDetailView, new_view, delete_view

app_name = "document"

urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<pk>/', DocumentDetailView.as_view(), name="detail"),
    path('new', new_view, name="new"),
    path('<id>/delete', delete_view, name="delete")
]

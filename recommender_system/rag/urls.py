from django.urls import path
from .views import RagQueryView

urlpatterns = [
    path("query/", RagQueryView.as_view()),
]

from .views import IndexView#, ServicesView, ContactView, TeamTemplate, DetailsView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

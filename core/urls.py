from .views import IndexView#, ServicesView, ContactView, TeamTemplate, DetailsView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # path('services', ServicesView.as_view(), name='Services'),
    # path('team', TeamTemplate.as_view(), name='Equipe'),
    # path('contact', ContactView.as_view(), name='Contact'),
    # path('details', DetailsView.as_view(), name='Detalhes')
]

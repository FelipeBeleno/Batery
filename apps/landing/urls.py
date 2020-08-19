from django.urls import path

from apps.landing.views import pruebaTemplateView

app_name = 'landige'

urlpatterns = [
    path('dashboard/', pruebaTemplateView.as_view(), name='prueba')
]

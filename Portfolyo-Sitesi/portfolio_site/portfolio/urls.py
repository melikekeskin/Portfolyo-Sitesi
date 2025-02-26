from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aziz_sancar/', views.aziz_sancar, name='aziz_sancar'),
    path('elon_musk/', views.elon_musk, name='elon_musk'),
    path('ada_lovelace/', views.ada_lovelace, name='ada_lovelace'),
    path('portfolio/', views.portfolio, name='portfolio'),
]

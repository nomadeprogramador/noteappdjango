from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('marcados/',views.notas_marcadas,name='marcadas'),
    path('excluir/<int:id>/',views.excluir_nota,name='excluir')
]
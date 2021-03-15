from django.urls import path

from . import views

urlpatterns = [
    path('crear/', views.crear),
    path('lista/', views.lista),
    path('usuario/<int:pk>', views.usuario),
    path('eliminar/<int:pk>', views.delete_buyer),
    path('geocodificar_base/', views.geocodificar_base),
]
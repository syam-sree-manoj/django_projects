from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:url_id>/', views.detail, name='detail'),
    path('<int:url_id>/results/', views.results, name='results'),
]
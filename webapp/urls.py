from django.urls import path
from webapp import views
from webapp.models import ConnectedUsers

urlpatterns = [
    path('online/', views.users_online),
    path('', views.index, name='index'),
    path('<str:article_id>/', views.room, name='article_id'),
]


ConnectedUsers.objects.all().delete()

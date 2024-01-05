from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("addTask/", views.addTask, name="addTask"),
    path("recieveTask/", views.recieveTask, name="recieveTask"),
    path("kill/", views.kill, name="kill"),
    path("choose/<int:key>/", views.choose, name="choice"),
    path("toDo/", views.toDo, name="toDO"),
    path('random/', views.randomF, name="random"),
    path("accept/<int:key>/", views.accept, name="accept"),
    path("decline/<int:key>/", views.decline, name="decline"),
    path("killHistory/", views.killHistory, name="killHistory"),
]
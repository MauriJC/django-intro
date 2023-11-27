from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('about',views.about),
    path('hello/<str:nombre>',views.queonda),
    path('projects',views.projects),
    path('tasks/<int:id>',views.tasks),
    path('tareas',views.tareas),
    path('proyectos',views.proyectos),
    path('create_task',views.create_task)
]
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('delete_complete', views.deleteCompleted, name='delete_complete'),
    path('delete_all', views.deleteAll, name='delete_all'),
]

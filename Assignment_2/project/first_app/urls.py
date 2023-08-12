from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('TaskModelpage/', views.TaskModel, name='TaskModelpage'),
    path('Show_tasks/', views.Show_tasks, name='Show_tasks'),
    path('Edit_button/<int:id>', views.Edit_button, name='Edit_button'),
    path('Delete_button/<int:id>', views.Delete_button, name='Delete_button'),
    path('Complete_button/<int:id>', views.Complete_button, name='Complete_button'),
]
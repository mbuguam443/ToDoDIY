from django.urls import path
from . import views


urlpatterns=[
    path('',views.Hompage,name="homapage"),
    path('submit',views.SubmitForm,name="submit"),
    path('todolist',views.TodoList,name="todolist"),
    path('delete/<int:id>',views.TodoDelete,name="delete"),
    path('searchData',views.TodoSearch,name="searchdata"),
    path('edit/<int:id>',views.TodoEdit,name="edit"),
    path('update',views.TodoUpdate,name="update")
]
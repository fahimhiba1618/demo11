from . import views
from django.urls import path

urlpatterns = [

     path('',views.add,name='add'),

    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update,name='update'),
    path('listhome/',views.TaskListView.as_view(),name='listhome'),
    path('detailhome/<int:pk>/',views.TaskDetailView.as_view(),name='detailhome'),
    path('updatehome/<int:pk>/',views.TaskUpdateView.as_view(),name='updatehome'),
    path('deletehome/<int:pk>/',views.TaskDeleteView.as_view(),name='deletehome'),
]


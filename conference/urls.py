from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='nn'),
        path('conference_list', views.conference_list, name='conference_list'),
        path('conference_content/<str:pk>', views.conference_content, name='conference_content'),
        path('conference_delete/<str:pk>', views.conference_delete, name='conference_delete'),
        path('project_list', views.project_list, name='project_list'),
        path('project_content/<str:pk>', views.project_content, name='project_content'),
        path('project_delete/<str:pk>', views.project_delete, name='project_delete'),
        path('error', views.eerror, name="eerror"),
]
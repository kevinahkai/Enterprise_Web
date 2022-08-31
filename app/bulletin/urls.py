from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index2'),
    path('topics/',views.topics,name='topics'),
    path('<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
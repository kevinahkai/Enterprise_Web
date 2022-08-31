from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('read', views.read, name='read'),
        path('detail/<str:pk>', views.detail, name="detail"),
        path('delete/<str:pk>', views.delete, name="delete"),
        path('error', views.eerror, name="eerror"),
        path("search/", views.SearchResults, name="search_results"),
]
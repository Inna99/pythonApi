from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('profile/', views.profile),
    path('languages/', views.LanguageListView.as_view(), name='languages'),
    path('languages/create/', views.LanguageCreate.as_view(), name='languages-create'),
    path('language/<str:pk>/update/', views.LanguageUpdate.as_view(), name='languages-update'),
    path('languages/<str:pk>/delete/', views.LanguageDelete.as_view(), name='languages-delete'),
]

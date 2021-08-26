from django.urls import path
from api import views


urlpatterns = [
    path('notes/', views.getData),
    path('notes/create/', views.createData),
    path('notes/<str:pk>/update/', views.updateData),
    path('notes/<str:pk>/delete/', views.deleteData),
    path('notes/<str:pk>/', views.viewDataById),
]

from django.urls import path
from convertlt import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('upload/', views.FileUploadView.as_view(), name='file-upload')
]
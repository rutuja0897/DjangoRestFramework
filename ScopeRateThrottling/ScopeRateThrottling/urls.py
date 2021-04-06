from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('studentapi/',views.StudentList.as_view()),
    path('studentapi/', views.StudentCreate.as_view()),
    #path('studentapi/', views.StudentRetrive.as_view()),
    #path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    #path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    #path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
    #path('studentapi/',views.ListCreateStudent.as_view()),
    #path('studentapi/<int:pk>/', views.RetriveUpdateStudent.as_view()),
    #path('studentapi/<int:pk>/', views.RetriveDestroyStudent.as_view()),
   # path('studentapi/',views.ListCreateStudent.as_view()),
   # path('studentapi/<int:pk>/', views.RetriveUpdateDestroyStudent.as_view()),
]

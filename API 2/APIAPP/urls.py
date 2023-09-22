from django.urls import path
from django.contrib import admin
from .views import FacultyList,SubjectList,StudentList,StudentDetails,FacultyDetails,SubjectDetails

urlpatterns = [
    path('api/faculty/',FacultyList.as_view()),
    path('api/faculty/<int:pk>/',FacultyDetails.as_view()),
    path('api/subject/',SubjectList.as_view()),
    path('api/subject/<int:pk>/',SubjectDetails.as_view()),
    path('api/student/',StudentList.as_view()),
    path('api/student/<int:pk>/',StudentDetails.as_view()),
    path('admin/', admin.site.urls),
]

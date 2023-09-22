from django.urls import path
from django.contrib import admin
from myapp.views import BookList,BookDetail
urlpatterns = [
    path('api/books',BookList.as_view()),
    path('api/books/<int:pk>',BookDetail.as_view()),
    path('admin/',admin.site.urls),
]
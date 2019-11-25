from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "myblogHome"),
    path('blogPost/<int:id>', views.blogPost, name = "blogPost"),

]

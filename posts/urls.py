from django.urls import path

from . import views

urlpatterns = [
    path('<slug>/', views.PostDetailUpdateView.as_view(), name='post_detail_view'),
]

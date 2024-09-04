from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/", views.author, name="author"),
    path("author/<int:author_id>/", views.author_about, name="author_about"),
    path("quote/", views.quote, name="quote"),
    path('tag/<str:tag_name>/', views.tags, name='tags'),
    path('tag/<str:tag_name>/page/<int:page>/', views.tags, name='tags_with_page'),
]
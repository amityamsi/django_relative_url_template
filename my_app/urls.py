from django.urls import path
from my_app import views

app_name='my_app'
urlpatterns=[
    path('',views.SchoolListView.as_view(),name='list'),
    path('?P<pk>-\d+',views.SchoolDetailView.as_view(),name='detail'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/?P<pk>-\d+',views.SchoolUpdateView.as_view(),name='update'),
     path('delete/?P<pk>-\d+',views.SchoolDeleteView.as_view(),name='delete'),
]
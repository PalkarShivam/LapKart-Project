from django.urls import path
from . import views
urlpatterns=[
    path('add/',views.add),
    path('show/',views.show),
    path('update/<j>/',views.update),
    path('delete/<k>/',views.delete),
]
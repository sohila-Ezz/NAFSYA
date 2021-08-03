from django.urls import path
from . import views
urlpatterns = [
    path('dates',views.showdates,name="dates"),
]
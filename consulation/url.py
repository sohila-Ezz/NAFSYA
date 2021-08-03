from django.urls import path
from . import views
urlpatterns = [
    path('consulation',views.showarconsulation,name="consulation"),
]
from django.urls import path
from . import views

app_name = 'predictor'

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("models/", views.models, name = "models"),
    path("model1/", views.model1, name = "model1"),
    path("model2/", views.model2, name = "model2"),
    path("model3/", views.model3, name = "model3")
    
]

from django.urls import path
from .views import test,lab_views,Lab_Detail
urlpatterns = [
    path("test",test,name="test!!!"),
    path("labapi/",lab_views.as_view()),
    path("labapi/<int:pk>",Lab_Detail.as_view())
    
]
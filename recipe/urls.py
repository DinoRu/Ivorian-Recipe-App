from django.urls import path
from .views import home, detail, CategoryView

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', detail, name='detail'),
    path('recipe/<slug:category>/', CategoryView.as_view(), name='recipe_by_category'),
]

from django.urls import path
from .views import SnackListView , SnackDetailView

# View modules

urlpatterns = [
    path('', SnackListView.as_view() , name='listView'),
    path('<int:pk>', SnackDetailView.as_view() , name='detail'),
]

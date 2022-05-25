from django.urls import path
from .views import HomePageView, SnackCreateView, SnackDeleteView, SnackUpdateView,  SnackDetailView, SnackDetailView

urlpatterns = [
  path ('', HomePageView.as_view(), name='snacklist'),

  path ('<int:pk>/', SnackDetailView.as_view(), name='snackdetail'),

  path ('create/', SnackCreateView.as_view(), name='snackcreate'),

  path ('<int:pk>/delete', SnackDeleteView.as_view(), name='snackdelete'),

  path ('<int:pk>/update', SnackUpdateView.as_view(), name='snackupdate'),
]

from django.urls import path
from dev_toolkit.apps.dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard_view'),
]